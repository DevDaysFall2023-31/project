from datetime import timedelta
import logging
from typing import List
import redis
from yandex_music import ClientAsync as YandexMusicClient, Track

log = logging.getLogger(__file__)


class TracksRepository:
    key = 'YA_MUSIC'
    limit = 20
    period = timedelta(seconds=2)

    def __init__(
        self,
        ya_music: YandexMusicClient,
        redis: redis.Redis,
    ):
        self.ya_music = ya_music
        self.redis = redis

    async def get_liked_tracks(self) -> List[Track]:
        tracks = await self.ya_music.users_likes_tracks(timeout=100)
        tracks = (await tracks.fetch_tracks_async()) if tracks else []
        return tracks

    async def get_similar_tracks(self, track_id: str) -> List[Track]:
        similar = await self.ya_music.tracks_similar(track_id, timeout=100)
        return similar.similar_tracks if similar else []

    async def download_track(self, track_id: str, path: str) -> None:
        log.info(f'downloading track {track_id} to {path}')
        if self.request_is_limited():
            log.warn(f'request is limited')
            return
        download_info = (await self.ya_music.tracks_download_info(track_id, timeout=100))[0]
        await download_info.download_async(path)

    async def like_track(self, track_id: str) -> None:
        await self.ya_music.users_likes_tracks_add(track_id)

    def request_is_limited(self) -> bool:
        if self.redis.setnx(self.key, self.limit):
            self.redis.expire(self.key, int(self.period.total_seconds()))
        bucket_val = self.redis.get(self.key)
        if bucket_val and int(bucket_val) > 0:
            self.redis.decrby(self.key, 1)
            return False
        return True
