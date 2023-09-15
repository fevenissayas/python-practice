#lab 5, question 3

x = eval (input ("enter a number: "))
summ = 0
while x >0:
    i = x % 10
    summ = summ + i # (summ =+ i)
    x = x //10 #(x //= 10)
print (summ)
