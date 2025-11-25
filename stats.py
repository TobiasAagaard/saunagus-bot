 
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