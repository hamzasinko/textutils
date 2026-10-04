"""Core text helpers for the textutils library.

Every function validates its input, handles empty strings, and carries type
hints so editors can offer completions.
"""

import re

__all__ = ["word_count", "character_count", "reverse", "capitalize_words"]

_WORD_START = re.compile(r"(?<!\S)\w")


def _validate_text(text: str) -> None:
    """Raise a TypeError if *text* is not a string.

    Args:
        text: The value to validate.

    Raises:
        TypeError: If *text* is not a :class:`str`.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, not {type(text).__name__}")


def word_count(text: str) -> int:
    """Count the words in *text*.

    Words are separated by any amount of whitespace, so runs of spaces,
    tabs, and newlines all act as a single separator.

    Args:
        text: The string to count words in.

    Returns:
        The number of words in *text*. An empty string returns ``0``.

    Raises:
        TypeError: If *text* is not a :class:`str`.

    Examples:
        >>> word_count("hello world")
        2
        >>> word_count("  spaced   out  ")
        2
        >>> word_count("")
        0
    """
    _validate_text(text)
    return len(text.split())


def character_count(text: str) -> int:
    """Count the characters in *text*, spaces included.

    Args:
        text: The string to count characters in.

    Returns:
        The number of characters in *text*. An empty string returns ``0``.

    Raises:
        TypeError: If *text* is not a :class:`str`.

    Examples:
        >>> character_count("hello")
        5
        >>> character_count("hi there")
        8
        >>> character_count("")
        0
    """
    _validate_text(text)
    return len(text)


def reverse(text: str) -> str:
    """Return *text* with its characters in reverse order.

    Args:
        text: The string to reverse.

    Returns:
        A new string holding the characters of *text* in reverse order. An
        empty string returns an empty string.

    Raises:
        TypeError: If *text* is not a :class:`str`.

    Examples:
        >>> reverse("stressed")
        'desserts'
        >>> reverse("abc")
        'cba'
        >>> reverse("")
        ''
    """
    _validate_text(text)
    return text[::-1]


def capitalize_words(text: str) -> str:
    """Uppercase the first character of every word in *text*.

    Only the first character of each word is changed; the rest of each word
    is left exactly as it was. Whitespace, including newlines, is preserved.

    Args:
        text: The string to transform.

    Returns:
        A new string with the first character of each word uppercased. An
        empty string returns an empty string.

    Raises:
        TypeError: If *text* is not a :class:`str`.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("hello WORLD")
        'Hello WORLD'
        >>> capitalize_words("it's fine")
        "It's fine"
        >>> capitalize_words("")
        ''
    """
    _validate_text(text)
    return _WORD_START.sub(lambda match: match.group(0).upper(), text)