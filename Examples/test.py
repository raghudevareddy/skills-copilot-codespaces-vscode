def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = fibonacci(n)
print(fib_numbers)