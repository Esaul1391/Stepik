class PermaDict:
    def __init__(self, data=None):
        self.data = data.copy() if data is not None else {}

    def keys(self):
        return iter(self.data.keys())

    def values(self):
        return iter(self.data.values())

    def items(self):
        return iter(self.data.items())

    def __getitem__(self, item):
        return self.data[item]

    def  __setitem__(self, key, value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


d = dict.fromkeys(range(100), None)
attrdict = PermaDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)










# class AttrDict:
#     def __init__(self, data=None):
#         self.data = data if data else {}
#
#     def __len__(self):
#         return len(self.data)
#
#     def __iter__(self):
#         return iter(self.data.keys())
#
#     def __getitem__(self, key):
#         return self.data[key]
#
#     def __getattr__(self, attr):
#         return self.data[attr]
#
#     def __setattr__(self, key, value):
#         self.data[key] = value
#
#     def __delattr__(self, item):
#         del self.data[item]
#

















# class CyclicList:
#     def __init__(self, iterable=None):
#         self.iterable = iterable
#         self.length = len()
#
#     def append(self, item):
#         return self.iterable.append(item)
#
#     def pop(self, index=None):
#         if index is None:
#             index = self.length - 1
#         else:
#             index %= self.length






# def log_for(logfile, date_str):
#     output_filename = f"log_for_{date_str}.txt"
#
#     with open(logfile, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
#         for line in input_file:
#             if line.startswith(date_str):
#                 # Extract the event part of the line (excluding the date)
#                 event_part = line[len(date_str):].strip()
#                 print(event_part, file=output_file)


# def non_closed_files(files):
#     open_files = []
#
#     for f in files:
#         if not f.closed:
#             open_files.append(f)
#
#     return open_files

# def print_file_content(filename):
#     try:
#         with open(filename, mode='r', encoding='utf-8') as file:
#             for line in file:
#                 print(line, end='')
#     except FileNotFoundError:
#         print('Файл не найден')

# class SparseArray:
#     def __init__(self, default):
#         self.default = default
#         self.data = {}
#
#     def __getitem__(self, item):
#         return self.data.get(item, self.default)
#
#     def __setitem__(self, key, value):
#         if value == self.default:
#             self.data.pop(key, None)
#         else:
#             self.data[key] = value


# class ReversedSequence:
#     def __init__(self, sequence):
#         self.sequence = sequence
#
#     def __len__(self):
#         return len(self.sequence)
#
#     def __iter__(self):
#         return reversed(self.sequence)
#
#     def __getitem__(self, item):
#         return reversed(self.sequence)[item]
