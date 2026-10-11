"""Tests for the public textutils API surface."""

import pytest

import textutils
from textutils import (
    capitalize_words,
    character_count,
    reverse,
    slugify,
    word_count,
)

ALL_FUNCTIONS = (word_count, character_count, reverse, capitalize_words, slugify)

EXPECTED_ALL = [
    "capitalize_words",
    "character_count",
    "reverse",
    "slugify",
    "word_count",
]


def test_all_lists_the_public_api() -> None:
    assert textutils.__all__ == EXPECTED_ALL


@pytest.mark.parametrize("name", EXPECTED_ALL)
def test_public_names_are_importable(name: str) -> None:
    assert hasattr(textutils, name)


@pytest.mark.parametrize("function", ALL_FUNCTIONS, ids=lambda f: f.__name__)
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
def test_non_string_input_raises_type_error(
    function: object, value: object, type_name: str
) -> None:
    """Every public function rejects non-string input with a helpful message."""
    with pytest.raises(TypeError, match=f"must be str, not {type_name}"):
        function(value)


def test_accepts_str_subclass() -> None:
    class MyStr(str):
        pass

    assert word_count(MyStr("hello world")) == 2
