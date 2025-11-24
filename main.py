from stats import get_book_text, total_num_words , count_unique_characters, sort_characters_dictonary

book = 'books/frankenstein.txt'

def main():
    text = get_book_text(book)
    word_count = total_num_words(text)
    char_count = count_unique_characters(text)
    sorted_chars = sort_characters_dictonary(char_count)

    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()