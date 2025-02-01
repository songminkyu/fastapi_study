from typing import Optional, List, Union
from pydantic import Field, validator, ValidationError, ValidationInfo, field_validator, BaseModel
from pydantic_settings import BaseSettings,SettingsConfigDict

# https://docs.pydantic.dev/latest/concepts/pydantic_settings/
class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env_ex", env_file_encoding="utf-8")
    db_host: str = Field(default="localhost")
    db_port: int = Field(default=3306)

    @field_validator('db_host', mode='before')
    def check_host(cls, host_input):
        if host_input == 'localhost':
            return '127.0.0.1'
        return host_input

    @field_validator('db_port')
    def check_port(cls, port_input):
        if port_input not in [12345, 3306]:
            raise ValueError("port error")
        return port_input

class ProjectConfig(BaseModel):
    project_name: str = 'likelihood'
    db_info: DBConfig = DBConfig()

config_data={
    "project_name":"likelihood project",
    "db_info":{
        'db_host':'localhost',
        'db_port':3306
    }
}

project_config=ProjectConfig(**config_data)
print(project_config)
print(project_config.db_info)
