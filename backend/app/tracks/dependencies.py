from typing import Annotated

from fastapi import Depends
import redis
from yandex_music import ClientAsync as YandexMusicClient
from app.dependencies import get_redis, get_yandex_music_client

from app.tracks.repository import TracksRepository


async def get_tracks_repository(
    ya_music: Annotated[YandexMusicClient, Depends(get_yandex_music_client)],
    redis: Annotated[redis.Redis, Depends(get_redis)],
) -> TracksRepository:
    return TracksRepository(ya_music, redis)
