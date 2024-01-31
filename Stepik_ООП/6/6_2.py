

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
