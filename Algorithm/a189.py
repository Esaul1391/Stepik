class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]


        return nums

s = Solution()
sp = [1, 2, 3, 4, 5, 6, 7]
print(s.rotate(sp, 3))
