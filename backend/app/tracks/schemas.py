from typing import List, Optional
from pydantic import BaseModel
from yandex_music import Track


class GetArtistSchema(BaseModel):
    id: int
    name: Optional[str]
    cover_url: Optional[str]


class GetTrackSchema(BaseModel):
    id: str
    title: Optional[str]
    artists: List[GetArtistSchema]
    cover_url: Optional[str]

    @classmethod
    def from_track(cls, track: Track) -> 'GetTrackSchema':
        return cls(
            id=track.track_id,
            title=track.title,
            artists=[
                GetArtistSchema(
                    id=artist.id,
                    name=artist.name,
                    cover_url=f'{artist.cover.uri[:-2]}200x200' if artist.cover and artist.cover.uri else None,
                ) for artist in track.artists
            ],
            cover_url=f'{track.cover_uri[:-2]}200x200' if track.cover_uri else None
        )


class GetTracksListSchema(BaseModel):
    count: int
    tracks: List[GetTrackSchema]

    @classmethod
    def from_track_list(cls, tracks: List[Track]) -> 'GetTracksListSchema':
        return cls(
            count=len(tracks),
            tracks=[
                GetTrackSchema.from_track(track) for track in tracks
            ]
        )
