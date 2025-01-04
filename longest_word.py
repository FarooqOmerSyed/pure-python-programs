#longest word in the list of words

lst_words = ['apple', 'banana', 'orange', 'pear', 'grape', 'pineapple']

def longest_word(lst):
    longest = ''
    for word in lst:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(lst_words)) # Output: pineapple