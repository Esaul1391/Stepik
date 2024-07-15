class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_i = nums[1]
        i_stop = last_i
        for i in nums[2:]:
            if i == i_stop:
                nums.pop(i)
            if nums[i] == nums[i-1]:
                i_stop = i