from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from yandex_music.exceptions import YandexMusicError
from app.tracks.dependencies import get_tracks_repository

from app.tracks.repository import TracksRepository

router = APIRouter(prefix="/tracks")


@router.get("/favourites")
async def get_favourite_tracks(
    tracks_repo: Annotated[TracksRepository, Depends(get_tracks_repository)],
) -> List[str]:
    try:
        return await tracks_repo.get_liked_tracks()
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err


@router.get("/{track_id}/similar")
async def get_similar_tracks(
    track_id: str,
    tracks_repo: Annotated[TracksRepository, Depends(get_tracks_repository)],
) -> List[str]:
    try:
        return await tracks_repo.get_similar_tracks(track_id)
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err