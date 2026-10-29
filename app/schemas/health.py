from typing import Literal

from app.schemas import ApiModel


class HealthResponse(ApiModel):
    status: Literal["UP"]
    version: str
    model_version: str
    data_version: str
