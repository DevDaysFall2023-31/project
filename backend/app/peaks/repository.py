import logging
from typing import Optional, List
from storage3._sync.file_api import ListBucketFilesOptions
from supabase.client import Client as SupabaseClient

log = logging.getLogger(__file__)


class PeaksRepository:
    def __init__(self, supabase_client: SupabaseClient):
        self.supabase = supabase_client
        self.bucket_name = "y_storage"

    def _get_url(self, id: str) -> str:
        return self.supabase.storage.from_(self.bucket_name).create_signed_url(
            path=f"{id}.mp3", expires_in=100500,
        )['signedURL']

    def get_peak(self, id: str) -> Optional[str]:
        uploaded: set = set(
            map(
                lambda d: d.get("name", None),
                self.supabase.storage.from_(self.bucket_name).list(
                    options={
                        "limit": 100500,
                    },
                ),
            )
        )
        log.info(uploaded)
        if f'{id}.mp3' not in uploaded:
            log.info(f'peak {id} not found')
            return None

        log.info(f'peak {id} found')
        return self._get_url(id)

    def add_peak(self, file: str, id: str):
        log.info(f'uploading peak {id}')
        self.supabase.storage.from_(self.bucket_name).upload(
            file=file, path=f"{id}.mp3", file_options={"content-type": "audio/mpeg"}
        )

    def get_peaks(self, ids: List[str]) -> List[Optional[str]]:
        uploaded: set = set(
            map(
                lambda d: d.get("name", None),
                self.supabase.storage.from_(self.bucket_name).list(
                    options={
                        "limit": 100500,
                    },
                ),
            )
        )

        def url_or_none(id: str):
            if f'{id}.mp3' not in uploaded:
                return None
            return self._get_url(id)

        return [url_or_none(id) for id in ids]
