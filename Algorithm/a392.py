class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ind = 0
        for i in t:
            if s_ind == len(s):
                break
            if s[s_ind] == i:
                s_ind += 1

        return len(s) == s_ind


s = Solution()

print(s.isSubsequence("abxc", "ahbgdc"))

print(dir(set))
