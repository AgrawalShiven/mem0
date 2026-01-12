from fastapi import APIRouter
from mem0.memory.main import Memory

from mem0.service.settings import get_settings
from mem0.service.state.memory_state import set_memory, is_initialized

router = APIRouter(prefix="/config", tags=["config"])


@router.get("/init")
def init_memory():
    if is_initialized():
        return {"status": "already_initialized"}

    settings = get_settings()

    mem0_config = settings.build_mem0_config()

    memory = Memory.from_config(mem0_config)
    set_memory(memory)

    return {
        "status": "initialized",
        "collection": settings.QDRANT_COLLECTION,
    }

from service.state.memory_state import is_initialized


@router.get("/status")
def status():
    return {"initialized": is_initialized()}


