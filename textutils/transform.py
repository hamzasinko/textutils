"""String-transforming helpers for textutils."""

import re

from ._validation import _ensure_str

__all__ = ["reverse", "capitalize_words", "slugify"]

_WORD_START = re.compile(r"(?<!\S)\w")


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
    _ensure_str(text)
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
        "It's Fine"
        >>> capitalize_words("")
        ''
    """
    _ensure_str(text)
    return _WORD_START.sub(lambda match: match.group(0).upper(), text)


def slugify(text: str) -> str:
    """Turn *text* into a URL-friendly slug.

    The input is lowercased, every run of characters outside ``a-z0-9``
    (spaces, punctuation, underscores, accents, ...) is replaced by a single
    hyphen, and leading/trailing hyphens are removed. Existing hyphens are
    kept as separators, so ``"well-known"`` stays ``"well-known"`` while
    ``"foo_bar"`` becomes ``"foo-bar"``.

    Args:
        text: The string to slugify.

    Returns:
        A slug containing only lowercase ASCII letters, digits, and internal
        hyphens. An empty string, or a string with no letters/digits,
        returns ``""``.

    Raises:
        TypeError: If *text* is not a :class:`str`.

    Examples:
        >>> slugify("Hello, World!")
        'hello-world'
        >>> slugify("  Hello, World! Open Source  ")
        'hello-world-open-source'
        >>> slugify("Python --- is fun")
        'python-is-fun'
        >>> slugify("Version 2.0 released")
        'version-2-0-released'
        >>> slugify("!!!")
        ''
    """
    _ensure_str(text)
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")
