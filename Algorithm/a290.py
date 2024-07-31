
class Solution(object):
    def wordPattern(self, pattern, s):
        pattern_dict = {}
        s_dict = {}
        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            word = s_list[i]

            if (p in pattern_dict and pattern_dict[p] != word) or (word in s_dict and s_dict[word] != p):
                return False

            pattern_dict[p] = word
            s_dict[word] = p

        return True


def test_word_pattern():
    sol = Solution()
    assert sol.wordPattern("abba", "dog cat cat dog") == True
    assert sol.wordPattern("abba", "dog cat cat fish") == False
    assert sol.wordPattern("aaaa", "dog dog dog dog") == True
    assert sol.wordPattern("abba", "dog dog dog dog") == False
    assert sol.wordPattern("abc", "dog cat fish") == True
    assert sol.wordPattern("abc", "dog dog dog") == False
    assert sol.wordPattern("abc", "dog cat dog") == False
    assert sol.wordPattern("abba", "dog cat cat") == False
    assert sol.wordPattern("abc", "dog cat fish fish") == False
    assert sol.wordPattern("", "") == True
    assert sol.wordPattern("a", "dog") == True
    assert sol.wordPattern("a", "dog cat") == False
    assert sol.wordPattern("aa", "dog dog") == True
    assert sol.wordPattern("aa", "dog cat") == False
    assert sol.wordPattern("ab", "dog dog") == False
    print("All tests passed!")

# Запуск тестов
test_word_pattern()