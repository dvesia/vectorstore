from pydantic import BaseModel

from splitters.splitter_type import SplitterType
from typing import Dict, Any, Optional, List


class SplitterConf(BaseModel):
    splitter_type: SplitterType
    chunk_size: Optional[int]
    args: Optional[List[Any]]
    kwargs: Optional[Dict[str, Any]]
