from pydantic import BaseModel


class GetPeakSchema(BaseModel):
    track_id: str
    download_url: str
