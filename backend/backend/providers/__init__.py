from .zhipu import ZhipuProvider
from .minimax import MiniMaxProvider
from .volcengine import VolcengineProvider

class AIProviderFactory:
    @staticmethod
    def get_provider(name: str, **kwargs):
        providers = {
            "zhipu": ZhipuProvider,
            "minimax": MiniMaxProvider,
            "volcengine": VolcengineProvider
        }
        return providers[name](**kwargs) if name in providers else None

__all__ = ["ZhipuProvider", "MiniMaxProvider", "VolcengineProvider", "AIProviderFactory"]
