from mem0 import Memory
from typing import Optional

_memory: Optional[Memory] = None


def set_memory(memory: Memory) -> None:
    global _memory
    _memory = memory


def get_memory() -> Memory:
    if _memory is None:
        raise RuntimeError("Memory not initialized. Call /config/init first.")
    return _memory


def is_initialized() -> bool:
    return _memory is not None

