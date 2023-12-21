def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                yield cleaned_line[:25] + '...' if len(cleaned_line) > 25 else cleaned_line



with open('data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_heders = next(line_values)
    line_dickts = (dict(zip(file_heders, data)) for data in line_values)

    res = (int(line['raisedAmt']) for line in line_dickts if line['round'] == 'a')
    total_sum = sum(res)
    print(total_sum)




# def filter_names(names, ignore_char, max_names):
#     gen1 = (n for n in names if n.lower()[1] != ignore_char)
#     for k in range(max_names):
#         yield gen1[k]
#
# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
# print(*filter_names(data, 'D', 3))
# def all_together(*args):
#     return (element for iterable in zip(args) for element in iterable)



# def count_iterable(iterable):
#     count = 0
#     res = sum(1 for i in iterable)
#     return res

# def is_prime(number):
#     res = list(i for i in range(1, number + 1) if number % i == 0)
#     if len(res) == 2:
#         return True
#     else:
#         return False

# cubes_of_odds = (i ** 3 for i in iterable if i%2 == 1)


# words = ['bee', 'stepik', 'geek']
#
# result = max(len(word) for word in words)
#
# print(result)


# def flatten(nested_list):
#     for i in nested_list:
#         if isinstance(i, list):
#             yield from flatten(i)
#         else:
#             yield i


# def bee():
#     yield from 'bee'
#
# def geek():
#     yield from 'geek'
#
# def beegeek():
#     yield from bee()
#     yield from geek()
#
# print(*beegeek())

# def reverse(sequence):
#     for i in range(len(sequence)):
#         yield sequence[-1]
#         sequence.pop()
#     return


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def primes(left, right):
#     current_number = max(2, left)
#
#     while current_number <= right:
#         if is_prime(current_number):
#             yield current_number
#         current_number += 1

# def simple_sequence():
#     num = 1
#     count = 1
#     while True:
#         yield num
#         count -=1
#         if count== 0:
#             num += 1
#             count = num


# def bee():
#     yield 'b'
#     yield 'e'
#     return 'e'
#
# next(bee())
# next(bee())
#
# print(next(bee()))
