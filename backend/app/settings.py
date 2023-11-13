from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    # TODO: remove token from here
    ya_token: str

    supabase_address: str
    supabase_key: str

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
    )
