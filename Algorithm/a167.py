class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(numbers)):
        #     for k in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[k] == target:
        #             return [i + 1, k + 1]
        # return []
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total > target:
                right -= 1
            if total < target:
                left += 1



s = Solution()
sp = [2, 3, 4]
print(s.twoSum(sp, 6))