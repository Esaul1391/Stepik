import unittest
from Algorithm.a1768 import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_both_words_same_length(self):
        word1 = "abc"
        word2 = "def"
        expected = "adbecf"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, expected)

    def test_word1_longer(self):
        word1 = "abcd"
        word2 = "xy"
        expected = "axbycd"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, expected)

    def test_word2_longer(self):
        word1 = "pq"
        word2 = "wxyz"
        expected = "pwqx"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, expected)

    def test_empty_word1(self):
        word1 = ""
        word2 = "mno"
        expected = "mno"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, expected)

    def test_empty_word2(self):
        word1 = "ijk"
        word2 = ""
        expected = "ijk"
        result = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()