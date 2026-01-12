from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any

from service.state.memory_state import get_memory

router = APIRouter(prefix="/memory", tags=["memory"])

class AddMemoryRequest(BaseModel):
    user_id: str
    content: str
    metadata: Optional[Dict[str, Any]] = None


class SearchMemoryRequest(BaseModel):
    user_id: str
    query: str
    limit: int = 5


@router.post("/add")
def add_memory(payload: AddMemoryRequest):
    try:
        memory = get_memory()
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

    result = memory.add(
        user_id=payload.user_id,
        content=payload.content,
        metadata=payload.metadata or {},
    )

    return {
        "status": "success",
        "memory": result,
    }


@router.post("/search")
def search_memory(payload: SearchMemoryRequest):
    try:
        memory = get_memory()
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

    results = memory.search(
        user_id=payload.user_id,
        query=payload.query,
        limit=payload.limit,
    )

    return {
        "status": "success",
        "results": results,
    }
