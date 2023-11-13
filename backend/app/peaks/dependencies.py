from typing import Annotated

from fastapi import Depends
from supabase.client import Client as SupabaseClient
from app.dependencies import get_supabase
from app.peaks.repository import PeaksRepository


async def get_peaks_repository(supabase: Annotated[SupabaseClient, Depends(get_supabase)]) -> PeaksRepository:
    return PeaksRepository(supabase)
