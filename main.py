
from .stats import total_num_words, count_unique_characters, sort_characters_dictonary
from .file_reader import get_book_text
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    word_count = total_num_words(text)
    char_count = count_unique_characters(text)
    sorted_chars = sort_characters_dictonary(char_count)

    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()