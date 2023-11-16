import logging
from typing import Optional, List
from supabase.client import Client as SupabaseClient

log = logging.getLogger(__file__)


class PeaksRepository:
    def __init__(self, supabase_client: SupabaseClient):
        self.supabase = supabase_client
        self.bucket_name = "y_storage"

    def get_peak(self, id: str) -> Optional[str]:
        uploaded: set = set(
            map(
                lambda d: d.get("name", None),
                self.supabase.storage.from_(self.bucket_name).list(),
            )
        )
        if f'{id}.mp3' not in uploaded:
            log.info(f'peak {id} not found')
            return None

        log.info(f'peak {id} found')
        return self.supabase.storage.from_(self.bucket_name).create_signed_url(
            path=f"{id}.mp3", expires_in=100500,
        )['signedURL']

    def add_peak(self, file: str, id: str):
        log.info(f'uploading peak {id}')
        self.supabase.storage.from_(self.bucket_name).upload(
            file=file, path=f"{id}.mp3", file_options={"content-type": "audio/mpeg"}
        )

    def get_peaks(self, ids: List[str]) -> List[Optional[str]]:
        return list(map(lambda id: self.get_peak(id), ids))
