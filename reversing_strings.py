x = 7654
def swap1 (x):
    lst = []
    summ = 0
    i = 1
    while x > 0:
        rem = x % 10
        summ += rem * i
        x //= 10
        i *= 10


    for i in range (len (x)):
        lst.append (x[i])
    
    y = x [0]
    z = x [len (x)-1]
    
    lst.pop (len (x)-1)
    lst.pop (0)
    lst. append (y)
    lst.insert (0, z)

    for i in range (len (lst)):
        print (lst[i], end = '')

swap1 (x)


def swap2 (x):
    lst = list (x)
    lst [0], lst [-1] = lst [-1], lst [0]
    for i in range (len (lst)):
        print (lst [i], end ='')
swap2 ('1234')
