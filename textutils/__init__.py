"""textutils: small, dependency-free helpers for common text tasks.

The whole public API is re-exported here, so one import is enough:

    >>> from textutils import word_count
    >>> word_count("hello world")
    2
"""

from .counting import character_count, word_count
from .transform import capitalize_words, reverse, slugify

__all__ = [
    "word_count",
    "character_count",
    "reverse",
    "capitalize_words",
    "slugify",
]

__version__ = "0.1.0"