from enum import Enum


class LoaderType(str, Enum):
    CSV = "csv"
    READ_THE_DOCS = "read_the_docs"
