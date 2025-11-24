# Bookbot

A Python command-line tool for analyzing text files. Bookbot provides  statistics about books like word count and character frequency analysis.

## Features

- **Word Count**: Count total words in any text file
- **Character Frequency Analysis**: Analyze and rank character occurrences
- **Command-Line Interface**: Easy to use with any book file

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd bookbot
```

2. Ensure you have Python 3 installed

## Usage

Run the analyzer on any text file:

```bash
python3 main.py <path_to_book>
```

Example:
```bash
python3 main.py books/mobydick.txt
```

## Project Structure

```
bookbot/
├── main.py           # Main entry point and CLI handler
├── stats.py          # Analysis functions
├── books/            # Sample books directory
│   └── frankenstein.txt
└── README.md
```
