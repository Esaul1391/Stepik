# st = input()
# print(*map(lambda x: float(int(x)), st.split(' ')), sep='\n')

# xs = [3, 140, 15, 92, 65, 100]
# max_index = max((0, 1, 2, 3, 4), key=lambda i: xs[i])
# print(max_index)

#
# number_names = {
#     0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#     10: 'ten', 11: 'eleven', 12: 'twelve',
#     13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
# print(*sorted(input().split(" "), key=lambda x: number_names[int(x)]))

# print(*map(lambda x: x[0], sorted(list(number_names.items()), key=lambda x: x[1])))

# def add_dollar_prefix(func):
#     def wrapper(*args, **kwargs):
#         result = str(func(*args, **kwargs))
#         return '$' + result
#     return wrapper
#
# @add_dollar_prefix
# def get_price(item):
#     prices = {'comic book': 5, 'puzzle': 20}
#     return prices[item]
#
# print(get_price(item='comic book'))


# def double(func):
#     def wrapper(*args, **kwargs):
#         doubled_result = func(*args, **kwargs) * 2
#         return doubled_result
#     return wrapper
#
# @double
# def get_color_code(color):
#     color_codes = {'black': '#000000', 'white': '#FFFFFF'}
#     return color_codes[color]
#
# print(get_color_code('white'))

