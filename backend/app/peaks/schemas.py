from typing import Optional
from pydantic import BaseModel


class GetPeakSchema(BaseModel):
    track_id: str
    download_url: Optional[str]
