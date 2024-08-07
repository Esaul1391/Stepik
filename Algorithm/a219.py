class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False

