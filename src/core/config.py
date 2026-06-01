from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/bookly"
    JWT_SECRET: str = "please-change-me"
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str = "redis://localhost:6379/0"

    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = ""
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "Bookly"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    DOMAIN: str = "localhost:8000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()

# Celery reads these module-level names through config_from_object().
broker_url = Config.REDIS_URL
result_backend = Config.REDIS_URL
broker_connection_retry_on_startup = True
