"""textutils: small, dependency-free helpers for common text tasks.

Public API:
    ``word_count``, ``character_count``, ``reverse``, ``capitalize_words``,
    ``slugify``.

Everything else (modules or names starting with ``_``) is internal and may
change without notice.
"""

from .counting import character_count, word_count
from .transform import capitalize_words, reverse, slugify

__all__ = [
    "capitalize_words",
    "character_count",
    "reverse",
    "slugify",
    "word_count",
]

__version__ = "0.1.0"
