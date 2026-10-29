"""환경 변수 설정. 서버 환경 변수나 로컬 `.env`(커밋하지 않음)에서 읽는다(양식 `.env.example`)."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # 계산 모델·시장 데이터 버전. 결과 재현용으로 응답에 함께 내려 준다(값 규칙은 #4·#6).
    model_version: str = "none"
    data_version: str = "none"


@lru_cache
def get_settings() -> Settings:
    return Settings()
