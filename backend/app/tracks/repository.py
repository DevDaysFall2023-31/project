from typing import List
from yandex_music import ClientAsync as YandexMusicClient, Track


class TracksRepository:
    def __init__(self, ya_music: YandexMusicClient):
        self.ya_music = ya_music

    async def get_liked_tracks(self) -> List[Track]:
        tracks = await self.ya_music.users_likes_tracks()
        tracks = (await tracks.fetch_tracks_async()) if tracks else []
        return tracks

    async def get_similar_tracks(self, track_id: str) -> List[Track]:
        similar = await self.ya_music.tracks_similar(track_id)
        return similar.similar_tracks if similar else []

    async def download_track(self, track_id: str, path: str) -> None:
        download_info = (await self.ya_music.tracks_download_info(track_id))[0]
        await download_info.download_async(path)
