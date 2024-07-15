class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        next_valid = 0
        for current in range(len(nums)):
            if nums[current] != val:
                nums[next_valid] = nums[current]
                next_valid += 1
        return next_valid

