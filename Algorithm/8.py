class Solution(object):
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        last_digit = None
        mult = 1
        for i in s:
            if last_digit == 0 and i == '-':
                mult = -1
            if i.isdigit():
                if


s = Solution()
st = '  45'
print(s.myAtoi(st))