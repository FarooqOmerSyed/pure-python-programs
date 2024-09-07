# Reverse a string 
# approach one

my_string = 'pythonprograms'

def reverse_string():
    reversed_string = my_string[::-1]
    print(reversed_string)

reverse_string()

# approach two

def string_reverse(my_string):
    empty_string = ""
    for char in my_string:
        empty_string = char + empty_string
    return empty_string

string_reversed = string_reverse(my_string)
print(string_reversed)