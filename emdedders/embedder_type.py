from enum import Enum


class EmbedderType(str, Enum):
    HUGGINGFACE_HUB = "huggingface_hub"
    OPENAI = "openai"
