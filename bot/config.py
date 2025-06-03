from pydantic import BaseSettings

class Settings(BaseSettings):
    token: str
    admin_id: int = 0
    db_url: str = "sqlite:///bot.db"

    class Config:
        env_file = ".env"

settings = Settings()
