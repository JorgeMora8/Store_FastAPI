from pydantic import BaseSettings

class Settings(BaseSettings): 
    database_host:str
    database_user:str
    database_password:str
    database_port:str
    database_name:str

    class Config: 
        env_file = "./.env"

setting = Settings()
