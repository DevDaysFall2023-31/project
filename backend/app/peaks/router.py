import asyncio

from typing import Annotated
from fastapi import APIRouter, Depends

from app.peaks.dependencies import get_peaks_repository, get_peaks_worker
from app.peaks.repository import PeaksRepository
from app.peaks.schemas import GetPeakSchema
from app.peaks.worker import PeaksWorker

router = APIRouter(prefix="/peaks")


@router.get("/{track_id}")
async def get_peak(
    track_id: str,
    peaks_repo: Annotated[PeaksRepository, Depends(get_peaks_repository)],
    peaks_worker: Annotated[PeaksWorker, Depends(get_peaks_worker)],
) -> GetPeakSchema:
    peak_url = peaks_repo.get_peak(track_id)

    if not peak_url:
        asyncio.create_task(peaks_worker.crop_audio(track_id))
        return GetPeakSchema(
            track_id=track_id,
            download_url=None,
        )

    return GetPeakSchema(
        track_id=track_id,
        download_url=peak_url,
    )
