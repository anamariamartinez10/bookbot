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

# This function takes ONE dictionary (which will be an item from your list)
# and returns the value (the number) that you want to sort by.
def sort_on(dictionary_item):
        return dictionary_item["num"]
   
            
# takes a dictionary of characters and their counts and returns a sorted list
def get_sorted_characters(character_count):
    
    character_dictionary_list = []

    # add new_character_dictionary to character_dictionary_list
    for char, num in character_count.items():
        if char.isalpha():
            character_dictionary = {"char" : char, "num" : num}
            character_dictionary_list.append(character_dictionary)
    
    character_dictionary_list.sort(reverse=True, key= sort_on)
    
    return character_dictionary_list