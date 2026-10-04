"""Pytest configuration: makes the project root importable.

pytest's default ``prepend`` import mode inserts the directory containing this
file at the front of ``sys.path``, so ``import textutils`` resolves to the
package in this repo whether you run ``pytest`` or ``python -m pytest``.
"""