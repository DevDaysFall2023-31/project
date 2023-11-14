import tempfile
from pydub import AudioSegment
from app.peaks.repository import PeaksRepository
from app.tracks.repository import TracksRepository

class PeaksWorker:
    SECOND: int = 1_000

    def __init__(self, tracks_repo: TracksRepository, peaks_repo: PeaksRepository):
        self.tracks_repo = tracks_repo
        self.peaks_repo = peaks_repo

    def _crop(self, path: str) -> str:
        song = AudioSegment.from_mp3(path)
        song_mid: int = len(song) // 2
        five_seconds: int = 5 * self.SECOND
        first_10_seconds = song[song_mid - five_seconds: song_mid + five_seconds]
        out_filename = path + '.cropped.mp3'
        first_10_seconds.export(out_f=out_filename, format="mp3")
        return out_filename

    async def crop_audio(self, track_id: str) -> None:
        with tempfile.TemporaryDirectory() as dir:
            full_filename: str = dir + '/' + track_id + '.mp3'
            await self.tracks_repo.download_track(track_id, full_filename)
            res_filename = self._crop(full_filename)
            self.peaks_repo.add_peak(res_filename, track_id)
