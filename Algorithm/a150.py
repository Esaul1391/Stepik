class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))

s = Solution()
print(s.reverseWords('hellow world'))