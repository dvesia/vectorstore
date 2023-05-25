from langchain.document_loaders.base import BaseLoader
from langchain.document_loaders import CSVLoader, ReadTheDocsLoader
from loaders.loader_conf import LoaderConf
from loaders.loader_type import LoaderType


LOADERS = {
    LoaderType.CSV: CSVLoader,
    LoaderType.READ_THE_DOCS: ReadTheDocsLoader,
}


def loader(conf: LoaderConf) -> BaseLoader:
    loader = LOADERS.get(conf.loader_type, None)
    if loader is None:
        raise ValueError(f"Unsupported loader type: {conf.loader_type}")

    args = conf.args or []
    kwargs = conf.kwargs or {}

    return loader(*args, **kwargs)
