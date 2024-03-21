def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        number = fibonacci(n-1) + fibonacci(n-2)
        return number

fibonacci(10)
