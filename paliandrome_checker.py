def pali (x):
    summ = 0
    while x > 0:
        r = x % 10
        summ = (summ * 10) + r
        x //= 10
    return (summ)

x = 323
y = x
if y == pali (x):
    print (True)
else:
    print (False)
