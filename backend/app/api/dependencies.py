from typing import Annotated

from fastapi import Depends
from yandex_music import ClientAsync

from app.settings import AppSettings


async def get_settings() -> AppSettings:
    return AppSettings()


async def get_yandex_music_token(settings: Annotated[AppSettings, Depends(get_settings)]) -> str:
    return settings.ya_token


async def get_yandex_music_client(ya_token: Annotated[str, Depends(get_yandex_music_token)]) -> ClientAsync:
    return await ClientAsync(ya_token).init()
