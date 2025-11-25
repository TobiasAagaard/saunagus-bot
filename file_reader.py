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
        print(f"Error: The file at {filepath} was not found.")
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