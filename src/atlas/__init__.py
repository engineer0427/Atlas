from .project import Atlas
from .types import NodeType

__all__ = ["Atlas", "NodeType", "Ingestor", "Linker", "Visualizer"]

def __getattr__(name):
    if name == "Ingestor":
        from .ingest import Ingestor
        return Ingestor
    if name == "Linker":
        from .link import Linker
        return Linker
    if name == "Visualizer":
        from .viz import Visualizer
        return Visualizer
    raise AttributeError(name)
