from typing import Optional, List, Union
from pydantic_settings import BaseSettings,SettingsConfigDict

# https://docs.pydantic.dev/latest/concepts/pydantic_settings/
class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env_ex", env_file_encoding="utf-8")
    db_host: str
    db_port: int

conf = DBConfig()
print(conf)
