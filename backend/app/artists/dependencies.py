from typing import Annotated

from fastapi import Depends
from yandex_music import ClientAsync as YandexMusicClient
from app.dependencies import get_yandex_music_client
from app.artists.repository import ArtistsRepository


async def get_artists_repository(ya_music: Annotated[YandexMusicClient, Depends(get_yandex_music_client)]) -> ArtistsRepository:
    return ArtistsRepository(ya_music)
