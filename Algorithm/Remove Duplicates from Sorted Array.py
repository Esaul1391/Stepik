class Solution(object):
    def removeDuplicates(self, nums):
        res = []
        last = nums[0]
        res.append(last)
        for item in nums[1:]:
            if item == last:
                continue
            res.append(item)
            last = item

        return len(res), res

s = Solution()
print(s.removeDuplicates([1, 1, 2]))
