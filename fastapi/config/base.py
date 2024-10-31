from pydantic_settings import BaseSettings,  SettingsConfigDict
from os import environ




class BaseComfig(BaseSettings):
    SECRETS_FILE_PATH: str
    # @property
    # def POSTGRES_URL(self):
    #     return f"db+postgresql://{self.POSTGRES_USER}:{read_pass(self.POSTGRES_PASSWORD_FILE)}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_USER}"
    
    # @property
    # def REDIS_URL(self):
    #     return f"redis://:{read_pass(self.REDIS_PASSWORD_FILE)}@redis:{self.REDIS_PORT}/0"

    model_config = SettingsConfigDict(environ)    
