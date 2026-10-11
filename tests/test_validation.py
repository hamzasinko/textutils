"""Tests for the private textutils._validation module."""

import pytest

from textutils._validation import _ensure_str


@pytest.mark.parametrize(
    "text", ["hello", "", " "], ids=["ascii", "empty", "whitespace"]
)
def test_ensure_str_accepts_strings(text: str) -> None:
    """Return None for string input."""
    assert _ensure_str(text) is None


@pytest.mark.parametrize(
    "value, type_name",
    [
        pytest.param(None, "NoneType", id="none"),
        pytest.param(42, "int", id="int"),
        pytest.param(3.14, "float", id="float"),
        pytest.param(["a"], "list", id="list"),
        pytest.param({"k": "v"}, "dict", id="dict"),
        pytest.param(b"bytes", "bytes", id="bytes"),
    ],
)
def test_ensure_str_rejects_non_strings(value: object, type_name: str) -> None:
    """Raise TypeError naming the offending type."""
    with pytest.raises(TypeError, match=f"must be str, not {type_name}"):
        _ensure_str(value)
