from emdedders.embedder_conf import EmbedderConf
from emdedders.embedder_type import EmbedderType


class HuggingfaceHubConf(EmbedderConf):
    embedder_type: EmbedderType = EmbedderType.HUGGINGFACE_HUB
    huggingfacehub_api_token: str
