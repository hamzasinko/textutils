"""Tests for textutils.transform."""

import pytest

from textutils import capitalize_words, reverse, slugify

# --- reverse ----------------------------------------------------------------

REVERSE_CASES = [
    pytest.param("stressed", "desserts", id="reverses-word"),
    pytest.param("ab c", "c ba", id="reverses-sentence"),
    pytest.param("AbC", "CbA", id="mixed-case"),
    pytest.param("", "", id="empty-string"),
    pytest.param("a", "a", id="single-character"),
    pytest.param("racecar", "racecar", id="palindrome-unchanged"),
    pytest.param("a\tb\n", "\nb\ta", id="reverses-tabs-and-newlines"),
    pytest.param("héllo", "olléh", id="unicode"),
    pytest.param("a\u0301b", "b\u0301a", id="combining-mark-order-flips"),
    pytest.param("abc" * 20_000, ("abc" * 20_000)[::-1], id="very-long-input"),
]


@pytest.mark.parametrize("text, expected", REVERSE_CASES)
def test_reverse(text: str, expected: str) -> None:
    """Return the characters in reverse order."""
    assert reverse(text) == expected


def test_reverse_does_not_mutate_input() -> None:
    """Return a new string and leave the input unchanged."""
    original = "abc"
    reverse(original)
    assert original == "abc"


# --- capitalize_words -------------------------------------------------------

CAPITALIZE_WORDS_CASES = [
    pytest.param("hello world", "Hello World", id="capitalizes-each-word"),
    pytest.param("hello WORLD", "Hello WORLD", id="leaves-rest-unchanged"),
    pytest.param("it's fine", "It's Fine", id="does-not-break-apostrophes"),
    pytest.param("a\tb", "A\tB", id="tab-is-a-separator"),
    pytest.param("", "", id="empty-string"),
    pytest.param(
        "  hello  world\nagain", "  Hello  World\nAgain", id="preserves-whitespace"
    ),
    pytest.param("Hello World", "Hello World", id="already-capitalized"),
    pytest.param("héllo wörld", "Héllo Wörld", id="unicode-word-start"),
    pytest.param("123 abc", "123 Abc", id="leading-digits"),
    pytest.param("!!!", "!!!", id="punctuation-only"),
    pytest.param("(hello)", "(hello)", id="not-after-whitespace"),
    pytest.param("well-known", "Well-known", id="hyphen-not-a-separator"),
]


@pytest.mark.parametrize("text, expected", CAPITALIZE_WORDS_CASES)
def test_capitalize_words(text: str, expected: str) -> None:
    """Uppercase the first character of each word."""
    assert capitalize_words(text) == expected


# --- slugify ----------------------------------------------------------------

SLUGIFY_CASES = [
    pytest.param("Hello, World!", "hello-world", id="punctuation-to-hyphen"),
    pytest.param(
        "  Hello, World! Open Source  ",
        "hello-world-open-source",
        id="collapses-repeated-spaces",
    ),
    pytest.param("Python --- is fun", "python-is-fun", id="collapses-repeated-hyphens"),
    pytest.param("Version 2.0 released", "version-2-0-released", id="keeps-digits"),
    pytest.param("", "", id="empty-string"),
    pytest.param("!!!", "", id="punctuation-only"),
    pytest.param("café au lait", "caf-au-lait", id="strips-non-ascii"),
    pytest.param("well-known", "well-known", id="keeps-existing-hyphen"),
    pytest.param("foo_bar", "foo-bar", id="underscore-to-hyphen"),
    pytest.param("HELLO", "hello", id="lowercases-input"),
    pytest.param("a\tb\nc", "a-b-c", id="tabs-and-newlines"),
    pytest.param("--Foo--", "foo", id="strips-leading-trailing-hyphens"),
    pytest.param("a" * 100_000, "a" * 100_000, id="very-long-input"),
]


@pytest.mark.parametrize("text, expected", SLUGIFY_CASES)
def test_slugify(text: str, expected: str) -> None:
    """Return a lowercase, hyphen-separated slug."""
    assert slugify(text) == expected
