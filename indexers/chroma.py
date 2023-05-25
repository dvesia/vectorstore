from langchain.vectorstores import Chroma
from indexers.indexer_conf import IndexerConf
from indexers.indexer_type import IndexerType
from typing import Optional, List
from pydantic import Field
from langchain.embeddings.base import Embeddings


class ChromaConf(IndexerConf):

    """
    Configuration class for Chroma indexer.

    Attributes:
        indexer_type (IndexerType): The type of indexer (CHROMA).
        embedding_function (str): The name of the embedding function.
        persist_directory (Optional[str]): The directory path where the vector DB will be persisted.
            If not specified, the vector DB will not be persisted on disk.
        args (Optional[list]): Additional arguments for the Chroma indexer (if required).
        kwargs (Optional[dict]): Additional keyword arguments for the Chroma indexer (if required).
    """

    indexer_type: IndexerType = IndexerType.CHROMA
    persist_directory: str

    def init(self, embedder: Embeddings, texts: List):
        """
        Initialize and index data using the Chroma indexer.

        Args:
            embedder (Embeddings): The embedding model.
            texts (List): List of texts/documents to be indexed.
        """

        Chroma.from_documents(texts, embedder, persist_directory=self.persist_directory)
