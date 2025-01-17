def fibonacci(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

n = 10  # You can change the value of n to get the first n Fibonacci numbers
result = fibonacci(n)
print(f"The first {n} Fibonacci numbers are {result}.")
