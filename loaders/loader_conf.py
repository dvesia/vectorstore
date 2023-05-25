from typing import List
from pydantic import BaseModel

from loaders.loader_type import LoaderType
from typing import Dict, Any, Optional


class LoaderConf(BaseModel):
    loader_type: LoaderType
    args: Optional[List[Any]]
    kwargs: Optional[Dict[str, Any]]
