x = eval (input ("enter a number: "))

def checkin (x):
    count = 0
    summ= 0
    y = x
    while y > 0:
        rem = y %10
        count += 1
        y //= 10
    y = x
    while y > 0:
         rrr = y % 10
         summ += (rrr **count)
         y //= 10
    return summ

if x == checkin (x):
     print (True)

else:
    print (False)
