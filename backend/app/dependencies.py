from typing import Annotated

from fastapi import Depends
from supabase.client import Client as SupabaseClient, create_client
from yandex_music import ClientAsync as YandexMusicClient

from app.settings import AppSettings


async def get_settings() -> AppSettings:
    return AppSettings()


async def get_yandex_music_token(settings: Annotated[AppSettings, Depends(get_settings)]) -> str:
    return settings.ya_token


async def get_yandex_music_client(ya_token: Annotated[str, Depends(get_yandex_music_token)]) -> YandexMusicClient:
    return await YandexMusicClient(ya_token).init()


async def get_supabase(settings: Annotated[AppSettings, Depends(get_settings)]) -> SupabaseClient:
    return create_client(settings.supabase_address, settings.supabase_key)
