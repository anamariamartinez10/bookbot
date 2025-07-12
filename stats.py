# accepts text from the book and returns the number of words in the string
def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words


# takes text from string and returns number of time each character appears in a string
def get_num_characters(file_contents):
    lower_case = file_contents.lower()

    # an empty dictionary
    character_count = {}

    for char in lower_case:
        # add char to character dictionary
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count
            

