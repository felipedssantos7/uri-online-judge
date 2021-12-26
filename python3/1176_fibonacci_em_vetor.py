# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
        
    x, y = 0, 1
    next = x + y
    for i in range(2, n):
        x = y
        y = next
        next = x + y
    
    return next


t = int(input())

for i in range(t):
    n = int(input())
    print("Fib({}) = {}".format(n, fibonacci(n)))
