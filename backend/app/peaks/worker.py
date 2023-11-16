import logging
import tempfile
import redis
import backoff
from pydub import AudioSegment
from yandex_music.exceptions import TimedOutError
from app.peaks.repository import PeaksRepository
from app.tracks.repository import TracksRepository

log = logging.getLogger(__file__)


class PeaksWorker:
    SECOND: int = 1_000

    def __init__(
        self,
        tracks_repo: TracksRepository,
        peaks_repo: PeaksRepository,
        redis: redis.Redis,
    ):
        self.tracks_repo = tracks_repo
        self.peaks_repo = peaks_repo
        self.redis = redis

    def _crop(self, path: str) -> str:
        song = AudioSegment.from_mp3(path)
        song_mid: int = len(song) // 2
        five_seconds: int = 2 * self.SECOND
        first_10_seconds = song[song_mid - five_seconds: song_mid + five_seconds]
        out_filename = path + '.cropped.mp3'
        first_10_seconds.export(out_f=out_filename, format="mp3")
        return out_filename

    async def _crop_audio(self, track_id: str) -> None:
        with tempfile.TemporaryDirectory() as dir:
            full_filename: str = dir + '/' + track_id + '.mp3'
            await self.tracks_repo.download_track(track_id, full_filename)
            res_filename = self._crop(full_filename)
            self.peaks_repo.add_peak(res_filename, track_id)

    @backoff.on_exception(
        backoff.expo,
        TimedOutError,
        max_time=60,
    )
    async def crop_audio(self, track_id: str) -> None:
        with self.redis.lock(f'crop-track-{track_id}', timeout=100):
            peak = self.peaks_repo.get_peak(track_id)
            if peak:
                log.info(f'stopping peak {track_id} crop as peak already exists')
                return

            await self._crop_audio(track_id)

