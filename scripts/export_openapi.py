"""OpenAPI 스키마를 `docs/contracts/openapi.json`으로 내보낸다.

uv run python -m scripts.export_openapi          # 파일 갱신
uv run python -m scripts.export_openapi --check # 파일이 코드와 다르면 실패(CI)
"""

import json
import sys
from pathlib import Path

from app.main import create_app

OUT = Path(__file__).resolve().parent.parent / "docs" / "contracts" / "openapi.json"


def render() -> str:
    return json.dumps(create_app().openapi(), ensure_ascii=False, indent=2) + "\n"


def main(argv: list[str]) -> int:
    content = render()
    if "--check" in argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != content:
            print(f"{OUT.name}가 코드와 다릅니다. export_openapi를 다시 실행하세요.")
            return 1
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
