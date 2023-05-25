from langchain.vectorstores import Pinecone

from indexers.indexer_conf import IndexerConf
from indexers.indexer_type import IndexerType
from typing import Optional, List
from pydantic import Field
import pinecone
from langchain.embeddings.base import Embeddings

import os


class PineconeConf(IndexerConf):
    """
    Configuration class for the Pinecone indexer.

    Attributes:
        indexer_type (IndexerType): The type of the indexer (set to IndexerType.PINECONE).
        api_key (str): The API key to authenticate with the Pinecone service.
        environment (str): The environment in which the Pinecone service is hosted.
        dimension (int): The dimensionality of the embeddings.
        index_name (str): The name of the index in the Pinecone service.
        text_key (List[str], optional): The key(s) in the document data that contain the text (default: ['texts']).
        embedding_function (str, optional): The name of the embedding function to be used (default: 'embedder').
        args (Optional[list], optional): Additional arguments for the indexer.
        kwargs (Optional[dict], optional): Additional keyword arguments for the indexer.
    """

    indexer_type: IndexerType = IndexerType.PINECONE
    api_key: str
    environment: str
    dimension: int
    index_name: str

    def init(self, embedder: Embeddings, texts: List):
        """
        Initializes the Pinecone indexer and loads documents.

        Args:
            embedder (Embeddings): An object representing the embedder.
            texts (List): A list of texts to be indexed.
        """

        # Initialize Pinecone
        pinecone.init(api_key=self.api_key, environment=self.environment)

        # Create an index
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(self.index_name, dimension=self.dimension)

        # Load documents
        Pinecone.from_texts(
            [t.page_content for t in texts], embedder, index_name=self.index_name
        )
