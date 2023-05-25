import yaml
import os
import logging

from etl.load_conf import LoadConf
from loaders.loader_type import LoaderType
from emdedders.embedder_type import EmbedderType
from indexers.indexer_type import IndexerType


def setup_logging():
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)

    # Set the log level for 'huggingface_hub.inference_api' logger to ERROR
    logging.getLogger("huggingface_hub.inference_api").setLevel(logging.ERROR)


def load_config():
    # Load config from file
    with open("conf/config.yaml", "r") as f:
        return LoadConf.parse_obj(yaml.safe_load(f))


def load_data(config):
    from loaders.loader import loader

    loader_type = yaml.safe_load(open("conf/config.yaml", "r"))["loader_type"]

    if loader_type == config.csv_loader_conf.loader_type:
        loader = loader(config.csv_loader_conf)
    elif loader_type == config.read_the_docs_loader_conf.loader_type:
        loader = loader(config.read_the_docs_loader_conf)

    else:
        raise ValueError(
            f"Invalid loader_type: {loader_type}. Possible values are: {', '.join(i.value for i in LoaderType)}"
        )

    logging.info("Loading data...")
    data = loader.load()
    logging.info(f"Loaded {len(data)} documents")
    return data


def split_data(config, data):
    from splitters.splitter import splitter

    splitter_type = yaml.safe_load(open("conf/config.yaml", "r"))["splitter_type"]

    if splitter_type == config.character_splitter_conf.splitter_type:
        splitter = splitter(config.character_splitter_conf)
    elif splitter_type == config.recursive_character_splitter_conf.splitter_type:
        splitter = splitter(config.recursive_character_splitter_conf)
    else:
        raise ValueError(
            f"Invalid splitter_type: {splitter_type}. Possible values are: {', '.join(i.value for i in LoaderType)}"
        )

    logging.info("Splitting data...")
    texts = splitter.split_documents(data)
    logging.info(f"Splitted into {len(texts)} chunks")
    return texts


def create_embedder(config, OPENAI_API_KEY, HUGGINGFACEHUB_API_TOKEN):
    from emdedders.embedder import embedder

    embedder_type = yaml.safe_load(open("conf/config.yaml", "r"))["embedder_type"]

    if embedder_type == EmbedderType.OPENAI:
        config.openai_embedder_conf.openai_api_key = OPENAI_API_KEY
        embedder = embedder(config.openai_embedder_conf)
    elif embedder_type == EmbedderType.HUGGINGFACE_HUB:
        config.huggingface_hub_embedder_conf.huggingfacehub_api_token = (
            HUGGINGFACEHUB_API_TOKEN
        )
        embedder = embedder(config.huggingface_hub_embedder_conf)
    else:
        raise ValueError(
            f"Invalid embedder_type: {embedder_type}. Possible values are: {', '.join(i.value for i in EmbedderType)}"
        )

    logging.info("Embedding data...")

    return embedder


def index_data(config, texts, embedder, PINECONE_API_KEY):
    from indexers.indexer import indexer

    indexer_type = yaml.safe_load(open("conf/config.yaml", "r"))["indexer_type"]

    if indexer_type == IndexerType.PINECONE:
        config.pinecone_conf.api_key = PINECONE_API_KEY
        indexer(config.pinecone_conf, texts, embedder)
    elif indexer_type == IndexerType.CHROMA:
        indexer(config.chroma_conf, texts, embedder)
    else:
        raise ValueError(
            f"Invalid indexer_type: {indexer_type}. Possible values are: {', '.join(i.value for i in IndexerType)}"
        )

    logging.info("Indexing data...")


def main():
    # Retrieve environment variables
    HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    setup_logging()
    config = load_config()
    data = load_data(config)
    texts = split_data(config, data)
    embedder = create_embedder(config, OPENAI_API_KEY, HUGGINGFACEHUB_API_TOKEN)
    index_data(config, texts, embedder, PINECONE_API_KEY)

    logging.info("All operations completed.")


if __name__ == "__main__":
    main()
