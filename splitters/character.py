from splitters.splitter_conf import SplitterConf

from splitters.splitter_type import SplitterType


class CharacterSplitterConf(SplitterConf):
    splitter_type: SplitterType = SplitterType.CHARACTER
    chunk_size: int
