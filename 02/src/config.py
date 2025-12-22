from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):    #This file is completely used for the env files being read automatically.
    DATABASE_URL : str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings()  #This object Config is used to access our .env 