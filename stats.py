from collections import Counter

def get_book_text(filepath):

    with open(filepath) as file:
        file_contents = file.read()
    
    return file_contents

def word_counter(string):
    return len(string.split())

def char_counter(string):
    characters = list(filter(lambda x: x != " ", string.lower()))
    char_count = Counter(characters)
    return dict(char_count)

def char_count_sorted(char_counted):
    list_of_char_counted = [{"char": k, "num": v} for k,v in char_counted.items()]
    list_of_char_counted.sort(reverse=True, key=lambda x: x["num"] ) 
    return list_of_char_counted


