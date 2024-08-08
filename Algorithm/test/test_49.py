import unittest
from Algorithm.a49 import Solution


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.func = Solution().groupAnagrams  # Replace with actual function call

    def test_example_case(self):
        # Test case from the problem statement
        input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertCountEqual(self.func(input_data), expected_output)

    def test_empty_string(self):
        # Test case with an empty string
        input_data = [""]
        expected_output = [[""]]
        self.assertCountEqual(self.func(input_data), expected_output)

    def test_single_letter_words(self):
        # Test case with single letter words
        input_data = ["a", "b", "c", "a"]
        expected_output = [["a", "a"], ["b"], ["c"]]
        self.assertCountEqual(self.func(input_data), expected_output)

    def test_mixed_case(self):
        # Test case with mixed case sensitivity
        input_data = ["abc", "bca", "CAB"]
        expected_output = [["abc", "bca"], ["CAB"]]
        self.assertCountEqual(self.func(input_data), expected_output)

    def test_no_anagrams(self):
        # Test case with no anagrams
        input_data = ["abc", "def", "ghi"]
        expected_output = [["abc"], ["def"], ["ghi"]]
        self.assertCountEqual(self.func(input_data), expected_output)

    def test_identical_words(self):
        # Test case with identical words
        input_data = ["abc", "abc", "abc"]
        expected_output = [["abc", "abc", "abc"]]
        self.assertCountEqual(self.func(input_data), expected_output)

    def test_large_input(self):
        # Test case with a large number of inputs
        input_data = ["".join(sorted("abcdefghijklmn"[i % 14:] + "abcdefghijklmn"[:i % 14])) for i in range(1000)]
        # Output not specified here, but should be groups of anagrams
        # This is just to test performance and handling of large inputs
        output = self.func(input_data)
        self.assertTrue(len(output) > 0)  # Ensure some output is generated

if __name__ == '__main__':
    unittest.main()