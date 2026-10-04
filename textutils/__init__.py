"""textutils: small, dependency-free helpers for common text tasks.

The whole public API is re-exported here, so one import is enough:

    >>> from textutils import word_count
    >>> word_count("hello world")
    2
"""

from .core import (
    capitalize_words,
    character_count,
    reverse,
    word_count,
)

__all__ = [
    "word_count",
    "character_count",
    "reverse",
    "capitalize_words",
]

__version__ = "0.1.0"