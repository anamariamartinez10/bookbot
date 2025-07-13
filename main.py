from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_characters
import sys

#new function to get filepath as input and return it's contents as a string
def get_book_text(filepath):
    # do something with f (the file) here
    with open(filepath) as f:
        # f is a file object
        # convert the book text to a string
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_characters = get_sorted_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
