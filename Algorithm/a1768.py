class Solution(object):
    def mergeAlternately(self, word1, word2):
        max_word = max(word1, word2, key=lambda x: len(x))
        min_word = min(word1, word2, key=lambda x: len(x))
        merge_sp = []
        for i in range(len(min_word)):
            merge_sp.append(word1[i])
            merge_sp.append(word2[i])
        return ''.join(merge_sp) + max_word[len(min_word):]
        # return len(min_word)


s = Solution()
print(s.mergeAlternately("abcd", "xy"))