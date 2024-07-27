from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d_magazine = Counter(magazine)
        for i in ransomNote:
            if i in d_magazine:
                d_magazine[i] -= 1
                if d_magazine[i] == 0:
                    d_magazine.pop(i)
            else:
                return False
        return True

s = Solution()
print(s.canConstruct('aa', 'aaab'))
