import asyncio

from typing import Annotated, List
from fastapi import APIRouter, Depends

from app.peaks.dependencies import get_peaks_repository, get_peaks_worker
from app.peaks.repository import PeaksRepository
from app.peaks.schemas import GetPeakSchema, GetPeakListSchema
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


@router.post("")
async def get_peaks(
    track_ids: List[str],
    peaks_repo: Annotated[PeaksRepository, Depends(get_peaks_repository)],
    peaks_worker: Annotated[PeaksWorker, Depends(get_peaks_worker)],
) -> GetPeakListSchema:
    peak_urls = peaks_repo.get_peaks(track_ids)

    if None in peak_urls:
        uncropped_ids = [track_ids[i] for i in range(len(track_ids)) if peak_urls[i] is None]
        asyncio.create_task(peaks_worker.crop_audio_files(uncropped_ids))

    return GetPeakListSchema(
        count=len(peak_urls),
        download_url=[
            GetPeakSchema(
                track_id=track_id,
                download_url=peak_url,
            ) for track_id, peak_url in zip(track_ids, peak_urls)
        ]
    )
