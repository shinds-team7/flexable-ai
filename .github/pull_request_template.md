## #️⃣ Issue

<!-- 이 PR이 처리하는 Issue. 예) Closes #12 -->
Closes #

## 📝 변경 내용

<!-- 무엇을 왜 바꿨는지. 어떻게보다 무엇·왜. -->

## 📚 참고한 문서

<!-- 기준으로 삼은 문서. 경로와 절을 적어 주세요. -->
- [ ] 이 저장소 docs/ (파일·절: )
- [ ] flexable-web docs/decisions/ (파일: )
- [ ] API 계약 (docs/contracts/openapi.json 등: )

## 🧩 영향받는 파트

- [ ] AI 서버 API·계약(→ flexable-web 호출 쪽 확인 필요)
- [ ] 계산 엔진(`app/engine/`)
- [ ] LLM(`app/llm/`)
- [ ] 배포·환경 변수

## 🧭 정책에 없어서 새로 내린 결정

<!-- 없으면 "없음". 다른 파트에 영향을 주면 flexable-web docs/decisions/에도 기록해 주세요. -->

## ✅ 검증 결과

<!-- 돌린 명령과 결과를 그대로. 확인하지 못한 것도 적어 주세요. -->
- [ ] `uv run ruff format --check . && uv run ruff check .`
- [ ] `uv run pyright`
- [ ] `uv run python -m scripts.export_openapi --check`
- [ ] `uv run pytest`
