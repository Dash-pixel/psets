def fibonacci(n):
    if n == 0:
        number = 1
        print(number)
        return number
    elif n == 1:
        number = 1
        print(number)
        return number
    else:
        print(number)
        number = fibonacci(n-1) + fibonacci(n-2)
        return number

fibonacci(3)
