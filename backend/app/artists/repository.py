from typing import List
from yandex_music import ClientAsync as YandexMusicClient, Track, Artist

class ArtistsRepository:
    def __init__(self, ya_music: YandexMusicClient):
        self.ya_music = ya_music

    async def get_artist_tracks(self, artist_id: str) -> List[Track]:
        tracks = (await self.ya_music.artists_tracks(artist_id=artist_id, timeout=100)).tracks
        return tracks

    async def search_artists(self, search: str) -> List[Artist]:
        artists = (await self.ya_music.search(text=search, type_='artist', timeout=100)).artists.results
        return artists
