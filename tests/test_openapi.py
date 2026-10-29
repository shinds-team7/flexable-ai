from scripts.export_openapi import OUT, render


def test_committed_openapi_matches_code() -> None:
    assert OUT.read_text(encoding="utf-8") == render(), (
        "docs/contracts/openapi.json이 코드와 다릅니다. "
        "`uv run python -m scripts.export_openapi`로 갱신하세요."
    )
