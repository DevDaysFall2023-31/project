from pydub import AudioSegment
from app.peaks.repository import PeaksRepository
from app.tracks.repository import TracksRepository

class PeaksWorker:
    SECOND: int = 1_000
    AUDIO_DIR: str = "audio"
    CROPPED_DIR: str = "cropped"

    def __init__(self, tracks_repo: TracksRepository, peaks_repo: PeaksRepository):
        self.tracks_repo = tracks_repo
        self.peaks_repo = peaks_repo

    def crop_audio(self, id: str):
        # TODO: download track from tracks repo

        full_filename: str = self.AUDIO_DIR + "/" + id
        song = AudioSegment.from_mp3(full_filename)
        song_mid: int = len(song) // 2
        five_seconds: int = 5 * self.SECOND
        first_10_seconds = song[song_mid - five_seconds: song_mid + five_seconds]
        first_10_seconds.export(out_f='/'.join([self.AUDIO_DIR, self.CROPPED_DIR, id]), format="mp3")

        # TODO: upload track to peaks repo
