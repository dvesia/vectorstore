from langchain.document_loaders.base import BaseLoader
from langchain.text_splitter import (
    CharacterTextSplitter,
    TokenTextSplitter,
    RecursiveCharacterTextSplitter,
    NLTKTextSplitter,
    SpacyTextSplitter,
    MarkdownTextSplitter,
    LatexTextSplitter,
    PythonCodeTextSplitter,
)

from splitters.splitter_conf import SplitterConf
from splitters.splitter_type import SplitterType


SPLITTERS = {
    SplitterType.CHARACTER: CharacterTextSplitter,
    SplitterType.RECURSIVE_CHARACTER: RecursiveCharacterTextSplitter,
}


def splitter(conf: SplitterConf) -> BaseLoader:
    loader = SPLITTERS.get(conf.splitter_type, None)
    if splitter is None:
        raise ValueError(f"Unsupported splitter type: {conf.splitter_type}")

    args = conf.args or []
    kwargs = conf.kwargs or {}

    return loader(*args, **kwargs)
