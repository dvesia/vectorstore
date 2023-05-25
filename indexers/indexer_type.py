from enum import Enum


class IndexerType(str, Enum):
    PINECONE = "pinecone"
    CHROMA = "chroma"
