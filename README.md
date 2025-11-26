# Bookbot

A Python command-line tool for analyzing text files. Bookbot provides  statistics about books like word count and character frequency analysis.

## Features

- **Word Count**: Count total words in any text file
- **Character Frequency Analysis**: Analyze and rank character occurrences
- **Command-Line Interface**: Easy to use with any book file
- **Global Installation**: Install once, use anywhere with the `bookbot` command

## Installation

### Option 1: Global Installation (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/TobiasAagaard/bookbot.git
cd bookbot
```

2. Install the package:
```bash
pip install -e .
```

3. Now use `bookbot` from anywhere:
```bash
bookbot books/frankenstein.txt
```

### Option 2: Direct Usage (Without Installation)

1. Clone the repository:
```bash
git clone https://github.com/TobiasAagaard/bookbot.git
cd bookbot
```

2. Run with Python directly:
```bash
python3 main.py books/frankenstein.txt
```

## Usage

### Using the installed command:
```bash
bookbot <path_to_book>
```

### Using Python directly:
```bash
python3 main.py <path_to_book>
```

### Examples:
```bash
bookbot ~/Documents/mybook.txt
python3 main.py books/mobydick.txt
```

## Uninstall

```bash
pip uninstall bookbot
```




