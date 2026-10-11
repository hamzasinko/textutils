"""Tests for textutils.counting."""

import pytest

from textutils import character_count, word_count

# --- word_count -------------------------------------------------------------

WORD_COUNT_CASES = [
    pytest.param("hello world", 2, id="counts-two-words"),
    pytest.param("one two three", 3, id="counts-three-words"),
    pytest.param("hello", 1, id="single-word"),
    pytest.param("", 0, id="empty-string"),
    pytest.param("   \t\n ", 0, id="whitespace-only"),
    pytest.param("  a   b  c ", 3, id="ignores-multiple-spaces"),
    pytest.param("a\tb\nc\r\nd", 4, id="tabs-and-newlines-separate-words"),
    pytest.param("  hi  ", 1, id="ignores-leading-trailing-whitespace"),
    pytest.param("!!!", 1, id="punctuation-only-is-one-token"),
    pytest.param("héllo wörld", 2, id="unicode-words"),
    pytest.param("Hello WORLD", 2, id="mixed-case"),
    pytest.param("word " * 10_000, 10_000, id="very-long-input"),
]


@pytest.mark.parametrize("text, expected", WORD_COUNT_CASES)
def test_word_count(text: str, expected: int) -> None:
    assert word_count(text) == expected


# --- character_count --------------------------------------------------------

CHARACTER_COUNT_CASES = [
    pytest.param("hello", 5, id="ascii"),
    pytest.param("hi there", 8, id="counts-spaces"),
    pytest.param("", 0, id="empty-string"),
    pytest.param(" \t\n", 3, id="whitespace-only"),
    pytest.param("a\tb\n", 4, id="counts-tabs-and-newlines"),
    pytest.param("héllo", 5, id="unicode-code-points"),
    pytest.param("👍", 1, id="emoji-single-code-point"),
    pytest.param("e\u0301", 2, id="combining-mark-counts-twice"),
    pytest.param("a" * 100_000, 100_000, id="very-long-input"),
]


@pytest.mark.parametrize("text, expected", CHARACTER_COUNT_CASES)
def test_character_count(text: str, expected: int) -> None:
    assert character_count(text) == expected
