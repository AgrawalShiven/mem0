from fastapi import FastAPI

from mem0.service.api.config import router as config_router
from mem0.service.api.memory import router as memory_router

app = FastAPI()

app.include_router(config_router)
app.include_router(memory_router)


@app.get("/health")
def health():
    return {"status": "ok"}

if _name_ == "_main_":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

