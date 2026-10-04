"""Tests for textutils.core."""

import pytest

from textutils import (
    capitalize_words,
    character_count,
    reverse,
    slugify,
    word_count,
)

ALL_FUNCTIONS = (word_count, character_count, reverse, capitalize_words, slugify)


class TestWordCount:
    """Tests for word_count."""

    def test_counts_words(self) -> None:
        assert word_count("hello world") == 2

    def test_single_word(self) -> None:
        assert word_count("hello") == 1

    def test_ignores_repeated_whitespace(self) -> None:
        assert word_count("  hello   world  ") == 2

    def test_newlines_separate_words(self) -> None:
        assert word_count("hello\nworld") == 2

    def test_empty_string(self) -> None:
        assert word_count("") == 0

    def test_whitespace_only(self) -> None:
        assert word_count("  \t\n ") == 0


class TestCharacterCount:
    """Tests for character_count."""

    def test_counts_characters(self) -> None:
        assert character_count("hello") == 5

    def test_counts_spaces(self) -> None:
        assert character_count("hi there") == 8

    def test_empty_string(self) -> None:
        assert character_count("") == 0

    def test_counts_unicode_characters(self) -> None:
        assert character_count("héllo") == 5


class TestReverse:
    """Tests for reverse."""

    def test_reverses_word(self) -> None:
        assert reverse("stressed") == "desserts"

    def test_reverses_sentence(self) -> None:
        assert reverse("ab c") == "c ba"

    def test_palindrome_is_unchanged(self) -> None:
        assert reverse("racecar") == "racecar"

    def test_empty_string(self) -> None:
        assert reverse("") == ""

    def test_single_character(self) -> None:
        assert reverse("a") == "a"

    def test_does_not_mutate_input(self) -> None:
        original = "abc"
        reverse(original)
        assert original == "abc"


class TestCapitalizeWords:
    """Tests for capitalize_words."""

    def test_capitalizes_each_word(self) -> None:
        assert capitalize_words("hello world") == "Hello World"

    def test_leaves_rest_of_word_unchanged(self) -> None:
        assert capitalize_words("hello WORLD") == "Hello WORLD"

    def test_does_not_break_apostrophes(self) -> None:
        assert capitalize_words("it's fine") == "It's Fine"

    def test_preserves_whitespace(self) -> None:
        assert capitalize_words("hello  world\nagain") == "Hello  World\nAgain"

    def test_already_capitalized(self) -> None:
        assert capitalize_words("Hello World") == "Hello World"

    def test_empty_string(self) -> None:
        assert capitalize_words("") == ""


class TestSlugify:
    """Tests for slugify."""

    def test_punctuation_becomes_hyphen(self) -> None:
        assert slugify("Hello, World!") == "hello-world"

    def test_repeated_spaces_collapse(self) -> None:
        assert slugify("  Hello, World! Open Source  ") == "hello-world-open-source"

    def test_repeated_hyphens_collapse(self) -> None:
        assert slugify("Python --- is fun") == "python-is-fun"

    def test_digits_kept(self) -> None:
        assert slugify("Version 2.0 released") == "version-2-0-released"

    def test_leading_trailing_symbols_removed(self) -> None:
        assert slugify("!!!") == ""

    def test_empty_string(self) -> None:
        assert slugify("") == ""

    def test_existing_hyphen_kept(self) -> None:
        assert slugify("well-known") == "well-known"

    def test_underscore_becomes_hyphen(self) -> None:
        assert slugify("foo_bar") == "foo-bar"

    def test_already_slug(self) -> None:
        assert slugify("hello-world") == "hello-world"

    def test_non_ascii_stripped(self) -> None:
        assert slugify("caf\u00e9 au lait") == "caf-au-lait"

    def test_lowercases_input(self) -> None:
        assert slugify("HELLO WORLD") == "hello-world"


@pytest.mark.parametrize("function", ALL_FUNCTIONS)
@pytest.mark.parametrize("value", [None, 42, 3.14, ["a"], {"k": "v"}, b"bytes"])
def test_non_string_input_raises_type_error(function: object, value: object) -> None:
    """Every public function rejects non-string input."""
    with pytest.raises(TypeError):
        function(value)