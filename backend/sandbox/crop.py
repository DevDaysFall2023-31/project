from app.settings import AppSettings
from pydub import AudioSegment
from dotenv import load_dotenv
from supabase import create_client, Client

import os

SECOND: int = 1_000
AUDIO_DIR: str = "audio"
CROPPED_DIR: str = "cropped"

def crop_audio(filename: str) -> None:
    full_filename: str = AUDIO_DIR + "/" + filename
    song = AudioSegment.from_mp3(full_filename)
    song_mid: int = len(song) // 2
    five_seconds: int = 5 * SECOND
    first_10_seconds = song[song_mid - five_seconds: song_mid + five_seconds]
    first_10_seconds.export(out_f='/'.join([AUDIO_DIR, CROPPED_DIR, filename]), format="mp3")


if __name__ == "__main__":
    settings = AppSettings()

    crop_audio("Mozart.mp3")

    supabase: Client = create_client(settings.supabase_address, settings.supabase_token)
    bucket_name: str = "test"

    data = supabase.storage.from_(bucket_name).list()

    for _, _, files in os.walk('/'.join([".", AUDIO_DIR, CROPPED_DIR])):
        uploaded: list = list(map(lambda d: d.get('name', None), supabase.storage.from_(bucket_name).list()))
        for file in files:
            if file not in uploaded:
                supabase.storage.from_(bucket_name).upload(
                    file='/'.join([".", AUDIO_DIR, CROPPED_DIR, file]),
                    path=file,
                    file_options={"content-type": "audio/mpeg"}
                )

    print(supabase.storage.from_(bucket_name).create_signed_url(path="Mozart.mp3", expires_in=60))
