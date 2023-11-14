from typing import List
from yandex_music import ClientAsync as YandexMusicClient


class TracksRepository:
    def __init__(self, ya_music: YandexMusicClient):
        self.ya_music = ya_music

    async def get_liked_tracks(self) -> List[str]:
        tracks = await self.ya_music.users_likes_tracks()
        tracks = tracks or []
        return [track.track_id for track in tracks]

    async def get_similar_tracks(self, track_id: str) -> List[str]:
        similar = await self.ya_music.tracks_similar(track_id)
        similar = similar or []
        return [track.track_id for track in similar]

    async def download_track(self, track_id: str, path: str):
        download_info = (await self.ya_music.tracks_download_info(track_id))[0]
        await download_info.download_async(path)
