import ebooklib
from ebooklib import epub

def get_book_text(filepath):
    try:
        if filepath.endswith('.epub'):
            return get_epub_text(filepath)
        with open(filepath, 'r') as file:
            filecontent = file.read()
        return filecontent
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.  ")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
    
def get_epub_text(filepath):
    try:
        book = epub.read_epub(filepath)
        text = ""
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                text += item.get_content().decode("utf-8")
        return text
    except Exception as e:
        print(f"Error reading EPUB file '{filepath}': {e}")
        return ""
    
def total_num_words(filecontent):
    words = filecontent.split()
    return len(words)

def count_unique_characters(filecontent):
    text = filecontent.lower()
    character_count = {}
    for char in text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sort_characters_dictonary(character_count):
    def sort_on(dictonary):
        return dictonary["num"]
    
    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list