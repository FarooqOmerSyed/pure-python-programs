import re

sentence = "happy python programmer python makes your life easy, python is great"

def count_words():
    user_input = input('Enter a word to search:').lower()
    matches = re.findall(user_input, sentence)
    print(f"The matches are {matches} and the count is {len(matches)}")

count_words()
