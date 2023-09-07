def sum_of_primes(x):
    summ = 0

    for i in range(2, x + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            summ += i

    return summ
if __name__ == "__main__":
    x = 10
    print(sum_of_primes(x))