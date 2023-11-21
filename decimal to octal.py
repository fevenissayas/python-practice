def decToOctal (x):
    suum = 0
    i = 1
    while x > 0:
        rem = x % 8
        suum = suum + rem * i
        x //= 8
        i = i * 10
    return suum
print (decToOctal (75))
