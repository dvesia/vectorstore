from abc import ABC, abstractmethod
import pydantic
from typing import Dict, Any, Optional, List

from langchain.embeddings.base import Embeddings
from indexers.indexer_type import IndexerType


class IndexerConf(pydantic.BaseModel, ABC):
    indexer_type: IndexerType
    args: Optional[List[Any]]
    kwargs: Optional[Dict[str, Any]]

    @abstractmethod
    def init(self, embedder: Embeddings, texts: List):
        ...
