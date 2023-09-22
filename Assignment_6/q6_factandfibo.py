#Factorial and Fibonacci in python

def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail_recursive(n - 1, n * accumulator)

result = factorial_tail_recursive(6)
print(result)

def fibonacci_tail_recursive(n, current=0, next=1):
    if n == 0:
        return current
    else:
        return fibonacci_tail_recursive(n - 1, next, current + next)

# Example usage:
result = fibonacci_tail_recursive(5)
print(result)
