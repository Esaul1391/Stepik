def get_pow(a, n):
    if n==0:
        return 1
    elif n==1:
        return a
    return a*(get_pow(a, n-1))
print(get_pow(5, 2))





# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция.')
#         message(times - 1)
#         print(times)
#
# message(5)


# def bee(n):
#     if n >= 7:
#         print('bee')
#     else:
#         print(n)
#         bee(n + 1)
#
#
# bee(4)


# def bee(n):
#     if n >= 7:
#         print('bee')
#     else:
#         bee(n + 1)
#         print(n)
#
#
# bee(4)