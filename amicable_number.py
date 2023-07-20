def amicable (x,y):
    summ = 0
    summ2 = 0
    for i in range (1, x+1):
        if x % i == 0:
            summ += i

    for j in range (1, y+1):
        if y % i == 0:
            summ2 += j

    if summ == summ2:
        print (True)
    else:
        print (False)

amicable (6,9)
