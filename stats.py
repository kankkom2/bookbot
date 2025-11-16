from collections import Counter

def get_book_text(filepath):

    with open(filepath) as file:
        file_contents = file.read()
    
    return file_contents

def word_counter(string):
    return len(string.split())


#   Takes in a string and filters away all of the characters that are not letters in a alphabet
def individual_word_counter(string):
    def filtered_on(string_element: str):
        accumulated = []
        for character in string_element:
            if character.isalpha():
                accumulated.append(True)
            else:
                accumulated.append(False)
        
        if accumulated.count(False) == len(accumulated):
            return False
        else:
            return True
    def sanitized_on(string_element):
        output = ""
        for char in string_element:
            if char.isalpha():
                output += char
        return output
    lowered = string.lower()
    words = list(filter(filtered_on, lowered.split()))
    clean_words = list(map(sanitized_on, words))
    return list(Counter(clean_words).items())




def char_counter(string):
    characters = list(filter(lambda x: x != " ", string.lower()))
    char_count = Counter(characters)
    return dict(char_count)

def char_count_sorted(char_counted):
    list_of_char_counted = [{"char": k, "num": v} for k,v in char_counted.items()]
    list_of_char_counted.sort(reverse=True, key=lambda x: x["num"] ) 
    return list_of_char_counted



if __name__ == "__main__":
    print(individual_word_counter( """
    Python is a programming language! Python's simplicity makes it powerful.
    :It's easy-to-learn, yet powerful. Don't you think so? I do!
    Python 3.8+ has new features; like the walrus operator := .
    """))