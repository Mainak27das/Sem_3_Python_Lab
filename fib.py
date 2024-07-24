def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_series(n):
    print("Fibonacci Series:", end=" ")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

# User input
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer")
else:
    generate_fibonacci_series(n)
