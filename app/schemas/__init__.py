"""API 요청·응답 스키마. JSON 필드는 Web 계약과 같은 camelCase로 내보낸다."""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
