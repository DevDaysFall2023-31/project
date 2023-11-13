from fastapi import FastAPI

from app.tracks.router import router as tracks_router
from app.peaks.router import router as peaks_router

app = FastAPI()
app.include_router(tracks_router)
app.include_router(peaks_router)
