from splitters.splitter_conf import SplitterConf
from splitters.splitter_type import SplitterType

from typing import List, Optional


class RecursiveCharacterSplitterConf(SplitterConf):
    splitter_type: SplitterType = SplitterType.RECURSIVE_CHARACTER
    chunk_size: Optional[int]
    chunk_overlap: Optional[int]
    separator: Optional[List[str]]
