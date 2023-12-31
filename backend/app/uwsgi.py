from fastapi import FastAPI

from app.tracks.router import router as tracks_router
from app.peaks.router import router as peaks_router
from app.playlists.router import router as playlists_router
from app.artists.router import router as artists_router

app = FastAPI()
app.include_router(tracks_router)
app.include_router(peaks_router)
app.include_router(playlists_router)
app.include_router(artists_router)
