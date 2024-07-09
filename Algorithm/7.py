class Solution(object):
    def reverse(self, x):
        new_num = 0
        count = x
        while x:
            r = x % 10
            x = x // 10
            new_num = new_num * 10 + r
            count -= 1
        return new_num


s = Solution()
num = -123
s.reverse(num)
