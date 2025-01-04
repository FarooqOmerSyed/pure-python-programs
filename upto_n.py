#write a python program that accepts an integer (n) and computes the value of n+nn+nnn

def upto_n3():
    usr_input = int(input("Enter your number : "))
    print(f"the user request number {usr_input} is calculated to {usr_input}+{usr_input}{usr_input}+{usr_input}{usr_input}{usr_input}")
    result = usr_input + (usr_input **2) + (usr_input**3)
    print(result)
    
upto_n3()