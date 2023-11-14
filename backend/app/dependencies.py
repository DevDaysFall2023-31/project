from typing import Annotated

from fastapi import Depends, HTTPException
from gotrue import UserResponse
from starlette import status
from supabase.client import Client as SupabaseClient, create_client
from yandex_music import ClientAsync as YandexMusicClient

from app.settings import AppSettings

from fastapi.security import OAuth2AuthorizationCodeBearer


supabase_auth = OAuth2AuthorizationCodeBearer(
    authorizationUrl="auth",
    tokenUrl="token",
)


async def get_settings() -> AppSettings:
    return AppSettings()


async def get_supabase(settings: Annotated[AppSettings, Depends(get_settings)]) -> SupabaseClient:
    return create_client(settings.supabase_address, settings.supabase_key)


def get_auth_user(
    token: Annotated[str, Depends(supabase_auth)],
    supabase: Annotated[SupabaseClient, Depends(get_supabase)],
) -> UserResponse:
    user = supabase.auth.get_user(token)
    if user:
        return user

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


async def get_yandex_music_token(user: Annotated[UserResponse, Depends(get_auth_user)]) -> str:
    return user.user.user_metadata.get('ya_token', '')


async def get_yandex_music_client(ya_token: Annotated[str, Depends(get_yandex_music_token)]) -> YandexMusicClient:
    return await YandexMusicClient(ya_token).init()
