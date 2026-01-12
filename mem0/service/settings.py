from pydantic_settings import BaseSettings
from pathlib import Path


def load_prompt(name: str) -> str:
    path = Path(__file__).parent / name
    return path.read_text(encoding="utf-8")


class Settings(BaseSettings):
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION: str = "mem0_memories"
    EMBEDDING_DIMS: int = 768

    LLM_PROVIDER: str = "gemini"
    LLM_MODEL: str = "gemini-3-flash-preview"
    LLM_TEMPERATURE: float = 0.0

    EMBEDDER_PROVIDER: str = "gemini"
    EMBEDDER_MODEL: str = "models/embedding-001"

    FACT_EXTRACTION_PROMPT: str = load_prompt("./custom_fact_extraction_prompt.txt")

    class Config:
        env_file = ".env"
        extra = "ignore"

    def build_mem0_config(self) -> dict:
        """
        Build a mem0-compatible config dict for Memory.from_config()
        """
        return {
            "llm": {
                "provider": self.LLM_PROVIDER,
                "config": {
                    "model": self.LLM_MODEL,
                    "temperature": self.LLM_TEMPERATURE,
                },
            },
            "embedder": {
                "provider": self.EMBEDDER_PROVIDER,
                "config": {
                    "model": self.EMBEDDER_MODEL,
                },
            },
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "url": self.QDRANT_URL,
                    "api_key": self.QDRANT_API_KEY,
                    "collection_name": self.QDRANT_COLLECTION,
                    "embedding_model_dims": self.EMBEDDING_DIMS,
                },
            },
            "custom_fact_extraction_prompt": self.FACT_EXTRACTION_PROMPT,
        }


def get_settings() -> Settings:

    return Settings()
