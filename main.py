# Function to find n'th Fibonacci number
def factorial(n):
    return 1 if (n < 1) else n * factorial(n - 1)
 
 
if __name__ == '__main__':
 
    n = 6
    print(f'The Factorial of {n} is', factorial(n))