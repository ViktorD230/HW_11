from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost/my_contacts_db"

def get_settings():
    return Settings()
