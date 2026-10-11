"""Private input-validation helpers for textutils."""


def _ensure_str(text: object) -> None:
    """Raise a ``TypeError`` if *text* is not a :class:`str`."""
    if not isinstance(text, str):
        raise TypeError(f"text must be str, not {type(text).__name__}")
