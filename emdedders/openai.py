from emdedders.embedder_conf import EmbedderConf
from emdedders.embedder_type import EmbedderType


class OpenaiConf(EmbedderConf):
    embedder_type: EmbedderType = EmbedderType.OPENAI
    openai_api_key: str
