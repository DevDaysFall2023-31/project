from typing import List, Optional
from pydantic import BaseModel
from yandex_music import Playlist


class GetPlaylistSchema(BaseModel):
    id: Optional[int]
    title: Optional[str]
    cover_url: Optional[str]

    @classmethod
    def from_playlist(cls, playlist: Playlist) -> 'GetPlaylistSchema':
        cover_url: Optional[str] = playlist.get_og_image_url()
        if cover_url == "https://":
            cover_url = None

        return cls(
            id=playlist.kind,
            title=playlist.title,
            cover_url=cover_url
        )


class GetPlaylistsListSchema(BaseModel):
    count: int
    playlists: List[GetPlaylistSchema]

    @classmethod
    def from_playlist_list(cls, playlists: List[Playlist]) -> 'GetPlaylistsListSchema':
        return cls(
            count=len(playlists),
            playlists=[
                GetPlaylistSchema.from_playlist(playlist) for playlist in playlists
            ]
        )
