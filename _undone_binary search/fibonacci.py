def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        number = fibonacci(n-1) + fibonacci(n-2)
        return number

fibonacci(10)

#solve without calling twice
# so fibonacci(n-1) contains fibonacci(n-2)

"""
how can we use dictionaries?
we can check whether the value already exists in a dictionary
"""
fib_dict = {}
def fib(n):
    #check for number in dictionary
    #n is the oder/index in fibonacci
    if n in fib_dict:
        return fib_dict[n]
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
