from typing import Union
import pydantic
from loaders import CSVLoaderConf, ReadTheDocsLoaderConf
from splitters import CharacterSplitterConf, RecursiveCharacterSplitterConf
from emdedders import HuggingfaceHubConf, OpenaiConf
from indexers import PineconeConf, ChromaConf


class LoadConf(pydantic.BaseModel):
    # loader_conf: Union[CSVLoaderConf, JSONLoaderConf]
    csv_loader_conf: CSVLoaderConf
    read_the_docs_loader_conf: ReadTheDocsLoaderConf
    # splitter_conf: Union[CharacterSplitterConf, RecursiveCharacterSplitterConf]
    character_splitter_conf: CharacterSplitterConf
    recursive_character_splitter_conf: RecursiveCharacterSplitterConf
    # embedder_conf: Union[HuggingfaceHubConf, OpenaiConf]
    huggingface_hub_embedder_conf: HuggingfaceHubConf
    openai_embedder_conf: OpenaiConf
    # indexer_conf: Union[PineconeConf, ChromaConf]
    pinecone_conf: PineconeConf
    chroma_conf: ChromaConf
