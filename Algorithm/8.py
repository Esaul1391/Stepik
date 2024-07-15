class Solution(object):
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        last_digit = None
        res = 0
        mult = 1
        for i in s:

            if i == '-' and last_digit is None:
                mult = -1

            if i.isdigit():
                last_digit = i
                # if int(i) == 0 and res == 0:
                #     continue
                res = (res * 10) + int(i)
            if i.isalpha():
                break
        return res * mult


s = Solution()
# st = '0-1'
st = '0-1'
print(s.myAtoi('0-1'))
print(s.myAtoi("words and 987"))