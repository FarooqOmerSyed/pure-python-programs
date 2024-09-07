# check if a string is a palindrome 

string_1 = 'hello'
string_2 = 'eollh'

def palindrome(string_1, string_2):
    if string_1 == string_2[::-1]:
        return True
    else:
        return False

print(palindrome(string_1, string_2))