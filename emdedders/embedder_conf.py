from pydantic import BaseModel

from emdedders.embedder_type import EmbedderType
from typing import Dict, Any, Optional, List


class EmbedderConf(BaseModel):
    embedder_type: EmbedderType
    args: Optional[List[Any]]
    kwargs: Optional[Dict[str, Any]]
