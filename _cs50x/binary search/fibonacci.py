def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        number = fibonacci(n - 1) + fibonacci(n - 2)
        return number


# I have no idea why i originally though i needed to make keys in dict a string

fib_dict = {}


def fib(n):
    # check for number in dictionary
    # n is the oder/index in fibonacci
    if n in fib_dict:
        return fib_dict[n]
    elif n == 0:
        fib_dict[n] = 1
        return 1
    elif n == 1:
        fib_dict[n] = 1
        return 1
    else:
        fib_num = fib(n - 1) + fib(n - 2)
        fib_dict[n] = fib_num
        return fib_num
