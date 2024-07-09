

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        l = 0

        # for r in range(len(s)):


        # if len(s) == 1:
        #     return 1
        # old_res = ''
        # res = ''
        # for i in s:
        #     if i in res:
        #         if len(old_res) < len(res):
        #             old_res = res
        #             res = ''
        #     if i not in res:
        #         res += i
        # if len(old_res) < len(res):
        #     old_res = res
        # return len(old_res)



s = Solution()
st = 'au'
print(s.lengthOfLongestSubstring(st))