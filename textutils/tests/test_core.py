"""Tests for textutils.core."""

import pytest

from textutils import capitalize_words, character_count, reverse, slugify, word_count


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
    assert reverse(text) == expected


def test_reverse_does_not_mutate_input() -> None:
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
    pytest.param("  hello  world\nagain", "  Hello  World\nAgain", id="preserves-whitespace"),
    pytest.param("Hello World", "Hello World", id="already-capitalized"),
    pytest.param("héllo wörld", "Héllo Wörld", id="unicode-word-start"),
    pytest.param("123 abc", "123 Abc", id="leading-digits"),
    pytest.param("!!!", "!!!", id="punctuation-only"),
    pytest.param("(hello)", "(hello)", id="not-after-whitespace"),
    pytest.param("well-known", "Well-known", id="hyphen-not-a-separator"),
]


@pytest.mark.parametrize("text, expected", CAPITALIZE_WORDS_CASES)
def test_capitalize_words(text: str, expected: str) -> None:
    assert capitalize_words(text) == expected


# --- slugify ----------------------------------------------------------------

SLUGIFY_CASES = [
    pytest.param("Hello, World!", "hello-world", id="punctuation-to-hyphen"),
    pytest.param("  Hello, World! Open Source  ", "hello-world-open-source", id="collapses-repeated-spaces"),
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
    assert slugify(text) == expected


# --- input validation -------------------------------------------------------

ALL_FUNCTIONS = (word_count, character_count, reverse, capitalize_words, slugify)

NON_STRING_VALUES = [
    pytest.param(None, "NoneType", id="none"),
    pytest.param(42, "int", id="int"),
    pytest.param(3.14, "float", id="float"),
    pytest.param(["a"], "list", id="list"),
    pytest.param({"k": "v"}, "dict", id="dict"),
    pytest.param(b"bytes", "bytes", id="bytes"),
]


@pytest.mark.parametrize("function", ALL_FUNCTIONS, ids=lambda f: f.__name__)
@pytest.mark.parametrize("value, type_name", NON_STRING_VALUES)
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
