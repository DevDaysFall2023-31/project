from typing import List
from yandex_music import ClientAsync as YandexMusicClient, Playlist, Track

import asyncio

class PlaylistsRepository:
    def __init__(self, ya_music: YandexMusicClient):
        self.ya_music = ya_music

    async def get_playlists(self) -> List[Playlist]:
        playlists = await self.ya_music.users_playlists_list(timeout=100)
        return playlists

    async def get_playlist_tracks(self, playlist_id: str) -> List[Track]:
        short_tracks = (await self.ya_music.users_playlists(kind=playlist_id, timeout=100)).tracks
        tasks = [short_track.fetch_track_async() for short_track in short_tracks]
        tracks = await asyncio.gather(*tasks)
        return tracks

    async def search_playlists(self, search: str) -> List[Playlist]:
        playlists = (await self.ya_music.search(text=search, type_='playlist', timeout=100)).playlists.results
        return playlists
