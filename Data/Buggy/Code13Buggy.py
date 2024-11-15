# # Buggy Code
# 
# def fibonacci(n):
#     if n > 0:
#         return "Input must be a non-negative integer."
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# 
# def factorial(n):
#     if n > 0:
#         return "Input must be a non-negative integer."
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

def fibonacci(n):
    if n < 0:
        return "Input must be a non-negative integer."
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n < 0:
        return "Input must be a non-negative integer."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)