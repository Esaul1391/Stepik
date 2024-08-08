from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict = defaultdict(list)
        for word in strs:
            sort_word = ''.join(sorted(word))
            anagrams_dict[sort_word].append(word)

        return list(anagrams_dict.values())