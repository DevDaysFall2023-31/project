from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from yandex_music.exceptions import YandexMusicError
from app.artists.dependencies import get_artists_repository

from app.artists.repository import ArtistsRepository
from app.artists.schemas import GetArtistsListSchema
from app.tracks.schemas import GetTracksListSchema

router = APIRouter(prefix="/artists")


@router.get("/{artist_id}/tracks")
async def get_artist_tracks(
    artist_id: str,
    artists_repo: Annotated[ArtistsRepository, Depends(get_artists_repository)],
) -> GetTracksListSchema:
    try:
        tracks = await artists_repo.get_artist_tracks(artist_id)
        return GetTracksListSchema.from_track_list(tracks)
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err

@router.get("")
async def search_artists(
    search: str,
    artists_repo: Annotated[ArtistsRepository, Depends(get_artists_repository)],
) -> GetArtistsListSchema:
    try:
        artists = await artists_repo.search_artists(search)
        return GetArtistsListSchema.from_artist_list(artists)
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err
