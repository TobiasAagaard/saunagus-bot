def get_book_text(filepath):
    with open(filepath, 'r') as file:
        filecontent = file.read()
    return filecontent


def total_num_words(filecontent):
    words = filecontent.split()
    return len(words)
