from stats import get_book_text, total_num_words , count_unique_characters

book = 'books/frankenstein.txt'

def main():
    text = get_book_text(book)
    print(f"Found {total_num_words(text)} total words")
    print(str(count_unique_characters(text)) + " unique characters")


main()