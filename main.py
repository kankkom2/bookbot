from stats import *
import sys


def main():
    if len(sys.argv) == 2:
        relative_path = sys.argv[1]
        book_text = get_book_text(relative_path)
        word_count = word_counter(book_text)
        char_count = char_counter(book_text)
        unique_words = individual_word_counter(book_text)
        
        list_of_char_count = [{k: v} for k,v in char_count.items()]
        

        sorted = char_count_sorted(char_count)
        #print([{k: v} for k,v in char_count.items()].sort(reverse=True, key=(lambda x: x)))
        print("=" * 12, "BOOKBOT", "=" * 12)
        print(f"Analyzing book found at {relative_path}...")
        print("-" * 12, "Word Count", "-" * 12)
        print(f'Found {word_count} total words')
        print("-" * 12, "Character Count", "-")
        for dictionay in sorted:
            if dictionay["char"].isalpha():
                print(dictionay["char"] + ":", dictionay["num"])
        
        print("-" * 12, "Unique Word Counter", "-" * 12)
        for word in unique_words:
            print(word[0] + ":", word[1])


        sys.exit(0)
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



if __name__ == "__main__":
    main()