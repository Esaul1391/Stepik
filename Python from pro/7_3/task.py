


# def add_to_list_in_dict(data, k, el):
#     try:
#         data[k].append(el)
#     except KeyError:
#         data[k] = [el]
#
#
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'b', 7)
#
# print(data)
file_name =''
try:
    with open(f'{file_name}', encoding='utf-8') as file:
        read_file = file.read()
        print(read_file)
except:
    'Файл не найден'