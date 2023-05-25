from langchain.embeddings.base import Embeddings
from langchain.embeddings import (
    HuggingFaceHubEmbeddings,
    OpenAIEmbeddings,
)

from emdedders.embedder_conf import EmbedderConf
from emdedders.embedder_type import EmbedderType


EMBEDDERS = {
    EmbedderType.HUGGINGFACE_HUB: HuggingFaceHubEmbeddings,
    EmbedderType.OPENAI: OpenAIEmbeddings,
}


def embedder(conf: EmbedderConf) -> Embeddings:
    """
    Creates and returns an instance of an embedding object
    based on the provided configuration.

    Args:
        conf (EmbedderConf):
        The configuration object specifying the embedding type and additional parameters.

    Returns:
        Embeddings: An instance of the embedding object.

    Raises:
        ValueError: If the provided embedding type is not supported.

    """

    embedder = EMBEDDERS.get(conf.embedder_type, None)

    if embedder is None:
        raise ValueError(f"Unsupported splitter type: {conf.embedder_type}")

    args = conf.args or []
    kwargs = conf.kwargs or {}

    return embedder(*args, **kwargs)
