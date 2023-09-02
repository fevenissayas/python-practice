
def fibb (x):
    lst = [0, 1]
    summ = 0
    for i in range (x):
        summ = lst [i] + lst [i+1]
        lst.append (summ)
    print (lst)
    return summ
print (fibb (5))