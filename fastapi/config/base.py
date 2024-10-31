from pydantic_settings import BaseSettings,  SettingsConfigDict
from os import environ

def read_pass(file_name):
    with open(file_name, 'r') as f:
        return f.read()




class BaseComfig(BaseSettings):
    SECRETS_FILE_PATH: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    PGDATA: str
    POSTGRES_PASSWORD: str
    @property
    def POSTGRES_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_USER}"
    
    # @property
    # def REDIS_URL(self):
    #     return f"redis://:{read_pass(self.REDIS_PASSWORD_FILE)}@redis:{self.REDIS_PORT}/0"

    model_config = SettingsConfigDict(environ)    
