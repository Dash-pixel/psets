def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        number = fibonacci(n-1) + fibonacci(n-2)
        return number

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
    if str(n) in fib_dict:
        return fib_dict[str(n)]
    elif n == 0:
        fib_dict[str(n)] = 1
        return 1
    elif n == 1:
        fib_dict[str(n)] = 1
        return 1
    else:
        fib_num = fib(n-1) + fib(n-2)
        fib_dict[str(n)] = fib_num
        return fib_num

for i in range(100):
    print(fib(i))
for j in range(100):
    print(fibonacci(j))
