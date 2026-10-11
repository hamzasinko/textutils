"""Word-counting helpers for textutils."""

from ._validation import _ensure_str

__all__ = ["word_count", "character_count"]


def word_count(text: str) -> int:
    """Count the words in *text*.

    Words are separated by any amount of whitespace, so runs of spaces,
    tabs, and newlines all act as a single separator.

    Parameters
    ----------
    text : str
        The string to count words in.

    Returns
    -------
    int
        The number of words in *text*. An empty string returns ``0``.

    Raises
    ------
    TypeError
        If *text* is not a :class:`str`.

    Examples
    --------
    >>> word_count("hello world")
    2
    >>> word_count("  spaced   out  ")
    2
    >>> word_count("")
    0
    """
    _ensure_str(text)
    return len(text.split())


def character_count(text: str) -> int:
    """Count the characters in *text*, spaces included.

    Parameters
    ----------
    text : str
        The string to count characters in.

    Returns
    -------
    int
        The number of characters in *text*. An empty string returns ``0``.

    Raises
    ------
    TypeError
        If *text* is not a :class:`str`.

    Examples
    --------
    >>> character_count("hello")
    5
    >>> character_count("hi there")
    8
    >>> character_count("")
    0
    """
    _ensure_str(text)
    return len(text)
