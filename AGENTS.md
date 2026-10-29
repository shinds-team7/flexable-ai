# 공통 개발 지침(flexable-ai)

텅장관리(Flex-able)의 AI·계산 서버다(FastAPI). 웹 화면·웹 서버·회원·목표·게임 세션은 [`shinds-team7/flexable-web`](https://github.com/shinds-team7/flexable-web)이 맡고, 이 서버는 Web 백엔드(Spring)만 호출하는 **무상태 계산·프리셋·설명 서비스**다. 브라우저·앱이 직접 부르지 않는다.

## 기준 문서

| 무엇 | 어디 |
|---|---|
| 제품 목적·범위·정책 | flexable-web [docs/PRD.md](https://github.com/shinds-team7/flexable-web/blob/main/docs/PRD.md), [docs/policies.md](https://github.com/shinds-team7/flexable-web/blob/main/docs/policies.md) |
| F7 목표 달성 개편 방향 | flexable-web [docs/decisions/2026-10-29-goal-scenarios.md](https://github.com/shinds-team7/flexable-web/blob/main/docs/decisions/2026-10-29-goal-scenarios.md) |
| 결정 기록 | 다른 파트에 영향을 주는 결정은 flexable-web `docs/decisions/` |
| 이 서버 API 스키마 | [docs/contracts/openapi.json](docs/contracts/openapi.json)(코드에서 생성, 정본 위치는 #8에서 확정) |

회의·메신저 합의와 채팅에 붙여 넣은 기획은 저장소 문서에 반영되기 전까지 개발 기준이 아니다.

## 작업 시작 전

- 이번 Issue의 목표·범위·완료 조건과 "결정 필요" 항목을 읽는다. 결정되지 않은 항목은 임의로 확정하지 않고 알린다.
- 관련 flexable-web 결정 기록을 저장소에서 직접 읽는다.

## 작업 중

- **숫자는 계산 엔진만 만든다.** LLM은 엔진이 만든 결과를 설명하거나 문장(가상 기업·뉴스)을 만들 뿐, 수익률·확률·가격을 새로 만들지 않는다.
- 계산 엔진(`app/engine/`)은 I/O 없는 순수 함수로 둔다. 같은 입력·`modelVersion`·`dataVersion`·`seed`면 같은 결과가 나와야 한다.
- 금액은 원 단위 정수, 나눗셈은 내림(Web ADR-3).
- JSON 필드는 camelCase(`app.schemas.ApiModel`). API는 `/v1` 아래에 둔다.
- 사용자 계정·식별자를 받지 않는다. 계산에 필요한 값만 받고, 요청 본문(목표 금액·성향 등)을 로그에 남기지 않는다.
- 네이버 뉴스 검색 결과는 LLM 입력·임베딩·학습·저장·파생 데이터에 쓰지 않는다(flexable-web `2026-10-28-event-news.md`).
- Web DB에 직접 접속하지 않는다. 데이터는 Web이 넘겨준다(#6).
- API를 바꾸면 `uv run python -m scripts.export_openapi`로 `docs/contracts/openapi.json`을 갱신한다.
- **공개 저장소다.** 비밀번호·키·개인 계정 정보를 코드·문서·커밋에 넣지 않는다. 값은 서버 환경 변수에 사람이 넣는다.

## 작업 완료 시

- 아래 검증 명령을 돌리고 결과를 그대로 보고한다.
- PR 템플릿을 채운다: Issue(`Closes #번호`), 참고한 문서, 영향받는 파트, 새로 내린 결정, 검증 결과.
- 브랜치는 `<종류>-<내용>`, 커밋은 `feat(ai): 한국어 요약`·`fix(ai): …` 형식이다. `main`에는 PR로 머지한다.

## 검증 명령

Python 3.12, [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run ruff format --check . && uv run ruff check .
uv run pyright
uv run python -m scripts.export_openapi --check
uv run pytest
```

## 하지 않는 것

- 운영 서버의 `.env`·배포를 직접 바꾸지 않는다.
- flexable-web의 DB·`.env`를 건드리지 않는다.
