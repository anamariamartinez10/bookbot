# accepts text from the book and returns the number of words in the string
def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words
