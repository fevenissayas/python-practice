def count_even (x):
    count = 0
    while x !=0:
        r = x%10
        if r % 2 == 0:
            count += 1
        x //= 10
    return count

x = int (input ("enter a number: "))
print (count_even (x))
