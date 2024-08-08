# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         print(f'Computing F{n} recursively...')
#         return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# print(fibonacci(7))

def fibonacci(n):
    if n <=1:
        return n
    fn = [0, 1]
    f1 = 0
    f2 = 1
    for i in range(2, n + 1):
        fn.append(fn[i - 2] + fn[i-1])
    return fn

print(fibonacci(150))