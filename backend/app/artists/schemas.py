from typing import List, Optional
from pydantic import BaseModel
from yandex_music import Artist


class GetArtistSchema(BaseModel):
    id: int
    name: Optional[str]
    cover_url: Optional[str]

    @classmethod
    def from_artist(cls, artist: Artist) -> 'GetArtistSchema':
        return cls(
            id=artist.id,
            name=artist.name,
            cover_url=f'{artist.cover.uri[:-2]}200x200' if artist.cover and artist.cover.uri else None
        )


class GetArtistsListSchema(BaseModel):
    count: int
    artists: List[GetArtistSchema]

    @classmethod
    def from_artist_list(cls, artists: List[Artist]) -> 'GetArtistsListSchema':
        return cls(
            count=len(artists),
            artists=[
                GetArtistSchema.from_artist(artist) for artist in artists
            ]
        )
