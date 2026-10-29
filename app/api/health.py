from typing import Annotated

from fastapi import APIRouter, Depends

from app import __version__
from app.config import Settings, get_settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, response_model_by_alias=True)
def health(settings: Annotated[Settings, Depends(get_settings)]) -> HealthResponse:
    """배포·모니터링용. 버전 없는 경로로 두고 인증 없이 응답한다."""
    return HealthResponse(
        status="UP",
        version=__version__,
        model_version=settings.model_version,
        data_version=settings.data_version,
    )
