from indexers.indexer_conf import IndexerConf
from indexers.indexer_type import IndexerType

from langchain.vectorstores.base import VectorStore
from langchain.embeddings.base import Embeddings

from langchain.vectorstores import (
    Pinecone,
    Chroma,
)

from typing import List

INDEXERS = {IndexerType.PINECONE: Pinecone, IndexerType.CHROMA: Chroma}


def indexer(conf: IndexerConf, texts: List, embedder: Embeddings) -> VectorStore:
    indexer = INDEXERS.get(conf.indexer_type, None)

    if indexer is None:
        raise ValueError(f"Unsupported indexer type: {conf.indexer_type}")

    # args = conf.args or []
    # kwargs = conf.kwargs or {}

    # return indexer(*args, **kwargs)
    return conf.init(texts=texts, embedder=embedder)
