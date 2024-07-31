import unittest
from Algorithm.a242 import Solution


class TestIsAnagram(unittest.TestCase):

    def test_anagrams(self):
        # Оба слова имеют одинаковые символы с одинаковой частотой
        self.assertTrue(Solution().isAnagram("anagram", "nagaram"))
        self.assertTrue(Solution().isAnagram("listen", "silent"))
        self.assertTrue(Solution().isAnagram("rat", "tar"))
        self.assertTrue(Solution().isAnagram("evil", "vile"))
        self.assertTrue(Solution().isAnagram("dusty", "study"))
        self.assertTrue(Solution().isAnagram("binary", "brainy"))

    def test_not_anagrams(self):
        # Слова не являются анаграммами
        self.assertFalse(Solution().isAnagram("hello", "billion"))
        self.assertFalse(Solution().isAnagram("world", "word"))
        self.assertFalse(Solution().isAnagram("apple", "pale"))
        self.assertFalse(Solution().isAnagram("rat", "car"))
        self.assertFalse(Solution().isAnagram("a", "ab"))

    def test_different_lengths(self):
        # Слова разной длины не могут быть анаграммами
        self.assertFalse(Solution().isAnagram("abc", "ab"))
        self.assertFalse(Solution().isAnagram("abcd", "abcde"))

    def test_empty_strings(self):
        # Пустые строки являются анаграммами друг друга
        self.assertTrue(Solution().isAnagram("", ""))

    def test_same_characters_different_count(self):
        # Слова с одинаковыми символами, но разным количеством
        self.assertFalse(Solution().isAnagram("aabb", "ab"))


if __name__ == '__main__':
    unittest.main()