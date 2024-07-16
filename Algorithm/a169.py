from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = Counter(nums)
        return d.most_common(1)[0][0]

s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
