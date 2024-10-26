def f(x):
    a = "aeiouAEIOU"
    b = ""
    for c in x:
        if c in a:
            b += c
        else:
            b = b
    return len(b) > 0

print(f("xyz"))