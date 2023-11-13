from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from yandex_music import ClientAsync
from yandex_music.exceptions import YandexMusicError

from app.api.dependencies import get_yandex_music_client

router = APIRouter(prefix="/api/v1")


@router.get("/tracks/{track_id}")
async def get_track(
    track_id: str,
    ya_music: Annotated[ClientAsync, Depends(get_yandex_music_client)],
) -> str:
    try:
        tracks = await ya_music.tracks([track_id])
        return tracks[0].title or ""
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err


@router.get("/tracks/{track_id}/similar")
async def get_similar_tracks(
    track_id: str,
    ya_music: Annotated[ClientAsync, Depends(get_yandex_music_client)],
) -> List[str]:
    try:
        tracks = await ya_music.tracks([track_id])
        similar = await ya_music.tracks_similar(tracks[0].track_id)
        similar = similar or []
        return [track.track_id for track in similar]
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err
