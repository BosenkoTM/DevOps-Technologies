
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@db:5432/fastapi_db"
    DEBUG: bool = True
    SECRET_KEY: str = "default_secret_key_change_this_in_production"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True

settings = Settings()
