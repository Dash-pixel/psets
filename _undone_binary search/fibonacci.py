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
        number = fibonacci(n-1)
        print(number)
        return number + fibonacci(n-2)

fibonacci(3)
