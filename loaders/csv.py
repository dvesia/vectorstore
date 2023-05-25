from loaders.loader_conf import LoaderConf

from loaders.loader_type import LoaderType


class CSVLoaderConf(LoaderConf):
    loader_type: LoaderType = LoaderType.CSV
    delimiter: str = ","
