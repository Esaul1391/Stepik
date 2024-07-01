class Solution(object):
    def mergeTwoLists(self, list1, list2):
        size_1 = len(list1)
        size_2 = len(list2)

        res = []

        i, j = 0, 0

        while i < size_1 and j < size_2:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        res = res + list1[i:] + list2[j:]
        return res

s = Solution()
s.mergeTwoLists([1, 4, 5, 6], [3, 5, 8])
print(s.mergeTwoLists([1, 4, 5, 6], [3, 5, 8]))