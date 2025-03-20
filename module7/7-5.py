from math import sqrt

def fib_explicit(n):
    """
    Calculate the nth Fibonacci number using the explicit formula.
    """
    return round(((1+sqrt(5))**n - (1-sqrt(5))**n) / (2**n * sqrt(5)),0)
    

def fib_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion."""
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)



if __name__ == "__main__":
    print("f50 (explicit) =", fib_explicit(8))
    # print("f50 (recursive) =", fib_recursive(50))