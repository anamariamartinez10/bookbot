from stats import get_num_words

#new function to get filepath as input and return it's contents as a string
def get_book_text(filepath):
    # do something with f (the file) here
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    # convert the book text to a string
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

main()
