from typing import Optional
from pydantic import BaseModel
from typing import List


class GetPeakSchema(BaseModel):
    track_id: str
    download_url: Optional[str]


class GetPeakListSchema(BaseModel):
    count: int
    peaks: List[GetPeakSchema]
