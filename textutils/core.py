"""Core text helpers for the textutils library.

Every function validates its input, handles empty strings, and carries type
hints so editors can offer completions.
"""

__all__ = ["word_count", "character_count"]


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