from typing import Annotated

from fastapi import Depends
from supabase.client import Client as SupabaseClient
from app.dependencies import get_redis, get_supabase
from app.peaks.repository import PeaksRepository
from app.peaks.worker import PeaksWorker
from app.tracks.dependencies import get_tracks_repository


async def get_peaks_repository(supabase: Annotated[SupabaseClient, Depends(get_supabase)]) -> PeaksRepository:
    return PeaksRepository(supabase)


async def get_peaks_worker(
    tracks_repo: Annotated[SupabaseClient, Depends(get_tracks_repository)],
    peaks_repo: Annotated[SupabaseClient, Depends(get_peaks_repository)],
    redis: Annotated[SupabaseClient, Depends(get_redis)],
) -> PeaksWorker:
    return PeaksWorker(tracks_repo, peaks_repo, redis)
