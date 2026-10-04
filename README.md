# textutils

Small, dependency-free Python helpers for common text tasks: counting words,
counting characters, reversing a string, and capitalizing each word. Every
function has type hints, a full docstring, and tests.

## Features

- `word_count(text)` — number of words in a string.
- `character_count(text)` — number of characters in a string.
- `reverse(text)` — the string reversed.
- `capitalize_words(text)` — first letter of each word capitalized.

Edge cases are handled: empty strings return empty results, and non-string
input raises `TypeError`.

## Installation

Clone it and run it locally:

```bash
git clone https://github.com/hamzasinko/textutils.git
cd textutils
python -m pytest
```

Requires Python 3.8 or newer. No third-party dependencies.

## Usage

```python
from textutils import word_count, character_count, reverse, capitalize_words

word_count("hello world") # 2
character_count("hello")          # 5
reverse("stressed")              # "desserts"
capitalize_words("hello world")   # "Hello World"
```

## Contributing

Contributions are welcome.

1. Fork the repository on GitHub.
2. Create a branch: `git checkout -b feature/my-change`.
3. Make your change, keeping commits small and focused.
4. Run the tests: `python -m pytest`.
5. Push your branch and open a pull request.

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.