from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "EduPath AI"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite+aiosqlite:///./edupath.db"
    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()