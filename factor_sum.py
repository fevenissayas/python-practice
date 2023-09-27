#lab 5, question 4

x = eval (input ("enter a number: "))
i = 1
summ = 0
while i <= x:
    if x % i == 0:
        summ += i
    i += 1
print (summ)
