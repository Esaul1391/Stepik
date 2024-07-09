

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        remain = 0
        res = []
        index = 0
        while index < len(l1) or index < len(l2):
            val1 = l1[index] if index < len(l1) else 0
            val2 = l2[index] if index < len(l2) else 0
            r = val1 + val2 + remain
            remain = 0
            if r > 9:
                r = r % 10
                remain = 1
            res.append(r)
            index += 1
        if remain:
            res.append(remain)

        return res



s = Solution()
list1 = [2, 8, 3, 5]
list2 = [5, 6, 4]
print(s.addTwoNumbers(list1, list2))





# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# print(selectionSort([5, 3, 6, 2, 10]))