import os
from pydantic_settings import BaseSettings

# Находим путь к папке, где лежит этот файл config.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    SECRET_KEY: str

    class Config:
        env_file = os.path.join(BASE_DIR, ".env") # это заставит Pydantic искать .env строго в папке backend

settings = Settings()