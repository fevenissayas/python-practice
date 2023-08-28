def factori (x):
    if x < 2:
        return 1

    f = x * factori(x-1)
    return f
print (factori (5))