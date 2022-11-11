from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_host: str = Field(env='POSTGRES_HOST')
    db_port: str = Field(env='POSTGRES_PORT')
    db_name: str = Field(env='POSTGRES_DB')
    db_user: str = Field(env='POSTGRES_USER')
    db_password: str = Field(env='POSTGRES_PASSWORD')


# settings = Settings(_env_file='.env')
