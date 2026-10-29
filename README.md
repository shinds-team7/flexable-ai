# flexable-ai

텅장관리(Flex-able) AI·계산 서버(FastAPI). Web 백엔드(Spring, [flexable-web](https://github.com/shinds-team7/flexable-web))만 호출한다.

| 맡는 것 | 맡지 않는 것(Web 백엔드) |
|---|---|
| 목표 달성 시뮬레이션 계산(#5), 공통 계산 엔진(#4), 가상 투자 프리셋 생성(#7), 계산 결과의 LLM 설명 | 회원·인증, 목표·성향 저장, 게임 세션·주문·체결, 화면 |

작업 방식은 [AGENTS.md](AGENTS.md)를 본다.

## 구조

```text
app/
  main.py        앱 생성, 라우터 연결
  config.py      환경 변수(.env.example)
  api/           HTTP 라우터(/health, /v1/...)
  schemas/       요청·응답 모델(camelCase)
  engine/        순수 계산 엔진
  llm/           LLM 어댑터
scripts/         OpenAPI 내보내기 등
tests/
docs/contracts/  openapi.json(코드에서 생성)
```

## 로컬에서 띄우기

Python 3.12와 [uv](https://docs.astral.sh/uv/)가 필요하다(uv가 3.12를 받아 준다).

```bash
uv sync
cp .env.example .env   # 필요할 때만
uv run uvicorn app.main:app --reload
curl -s localhost:8000/health
```

API 문서는 `http://localhost:8000/docs`.

## 검증

```bash
uv run ruff format --check . && uv run ruff check .
uv run pyright
uv run python -m scripts.export_openapi --check
uv run pytest
```

## 환경 변수

| 이름 | 설명 | 기본값 |
|---|---|---|
| `MODEL_VERSION` | 계산 모델 버전. `/health`와 계산 결과에 함께 나간다 | `none` |
| `DATA_VERSION` | 시장 데이터 버전 | `none` |

배포는 #2에서 정한다.
