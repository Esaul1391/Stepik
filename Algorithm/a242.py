from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = Counter(s)
        t_dict = Counter(t)
        return s_dict == t_dict