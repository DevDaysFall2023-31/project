from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from yandex_music.exceptions import YandexMusicError
from app.playlists.dependencies import get_playlists_repository

from app.playlists.repository import PlaylistsRepository
from app.playlists.schemas import GetPlaylistsListSchema
from app.tracks.schemas import GetTracksListSchema

router = APIRouter(prefix="/playlists")


@router.get("/my")
async def get_my_playlists(
    playlists_repo: Annotated[PlaylistsRepository, Depends(get_playlists_repository)],
) -> GetPlaylistsListSchema:
    try:
        playlists = await playlists_repo.get_playlists()
        return GetPlaylistsListSchema.from_playlist_list(playlists)
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err

@router.get("/{playlist_id}/tracks")
async def get_playlist_tracks(
    playlist_id: str,
    playlists_repo: Annotated[PlaylistsRepository, Depends(get_playlists_repository)],
) -> GetTracksListSchema:
    try:
        tracks = await playlists_repo.get_playlist_tracks(playlist_id)
        return GetTracksListSchema.from_track_list(tracks)
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err

@router.get("")
async def search_playlists(
    search: str,
    playlists_repo: Annotated[PlaylistsRepository, Depends(get_playlists_repository)],
) -> GetPlaylistsListSchema:
    try:
        playlists = await playlists_repo.search_playlists(search)
        return GetPlaylistsListSchema.from_playlist_list(playlists)
    except YandexMusicError as err:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=str(err),
        ) from err


