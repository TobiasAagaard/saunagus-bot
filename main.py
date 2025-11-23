from stats import get_book_text, total_num_words 


def main():
    print(f"Found {total_num_words(get_book_text('books/frankenstein.txt'))} total words")


main()