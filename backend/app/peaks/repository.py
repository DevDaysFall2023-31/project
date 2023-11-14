from typing import Optional
from supabase.client import Client as SupabaseClient


class PeaksRepository:
    def __init__(self, supabase_client: SupabaseClient):
        self.supabase = supabase_client
        self.bucket_name = "test"

    def get_peak(self, id: str) -> Optional[str]:
        uploaded: list = list(
            map(
                lambda d: d.get("name", None),
                self.supabase.storage.from_(self.bucket_name).list(),
            )
        )
        if f'{id}.mp3' not in uploaded:
            return None

        return self.supabase.storage.from_(self.bucket_name).create_signed_url(
            path=f"{id}.mp3", expires_in=60
        )['signedURL']

    def add_peak(self, file: str, id: str):
        self.supabase.storage.from_(self.bucket_name).upload(
            file=file, path=f"{id}.mp3", file_options={"content-type": "audio/mpeg"}
        )
