import asyncio

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.peaks.dependencies import get_peaks_repository
from app.peaks.repository import PeaksRepository
from app.peaks.worker import PeaksWorker
from app.tracks.dependencies import get_tracks_repository
from app.tracks.repository import TracksRepository

router = APIRouter(prefix="/peaks")


@router.get("/{track_id}")
async def get_peak(
    track_id: str,
    peaks_repo: Annotated[PeaksRepository, Depends(get_peaks_repository)],
    tracks_repo: Annotated[TracksRepository, Depends(get_tracks_repository)],
) -> str:
    peak_url = peaks_repo.get_peak(track_id)

    if not peak_url:
        worker = PeaksWorker(tracks_repo, peaks_repo)
        asyncio.create_task(worker.crop_audio(track_id))

        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
        )

    return peak_url
