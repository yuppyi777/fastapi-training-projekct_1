from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    APP_NAME: str = "FastAPI Demo App"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # 未定義の環境変数を無視（docker-compose.yml用の変数など）


settings = Settings()
