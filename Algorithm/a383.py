class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_dict = dict()
        for i in magazine:
            m_dict.setdefault(i, 0)
            m_dict[i] += 1
        return m_dict

s = Solution()
print(s.canConstruct('a', 'aaab'))
