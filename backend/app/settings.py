from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    supabase_address: str
    supabase_key: str

    redis_host: str
    redis_port: int
    redis_password: str

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
    )
