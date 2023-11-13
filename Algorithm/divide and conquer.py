# def sum(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
#
#
# print(sum([1, 2, 3, 4, 5, 6, 7]))

def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i < pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
