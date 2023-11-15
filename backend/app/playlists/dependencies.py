from typing import Annotated

from fastapi import Depends
from yandex_music import ClientAsync as YandexMusicClient
from app.dependencies import get_yandex_music_client
from app.playlists.repository import PlaylistsRepository


async def get_playlists_repository(ya_music: Annotated[YandexMusicClient, Depends(get_yandex_music_client)]) -> PlaylistsRepository:
    return PlaylistsRepository(ya_music)
