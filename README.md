# ⚡ TextPulse

`TextPulse` is a lightweight, command-line text statistics and formatting utility built in Python. It provides quick insights into text documents and transforms text strings across multiple programming case conventions without external dependencies.

## Features
- **Readability Stats:** Instantly computes word counts, character counts, and estimated reading times.
- **Case Transmuter:** Converts text between `snake_case`, `camelCase`, `PascalCase`, `kebab-case`, and `Title Case`.
- **Keyword Frequency:** Identifies core terms while filtering out common stop words.

## Usage

Run the script from your terminal:

```bash
python main.py "Software engineering students building clean Python utilities" --case snake --freq