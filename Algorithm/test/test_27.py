import unittest
from Algorithm.a27 import Solution

class TestRemoveElement(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()  # Создаем экземпляр класса Solution для использования в тестах

    def test_basic_case(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_length = 2
        expected_nums = [2, 2]  # Ожидаемый массив после удаления элементов val
        result = self.sol.removeElement(nums, val)  # Вызываем метод removeElement
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:expected_length], expected_nums)

    def test_empty_array(self):
        nums = []
        val = 5
        expected_length = 0
        expected_nums = []
        result = self.sol.removeElement(nums, val)
        self.assertEqual(result, expected_length)
        self.assertEqual(nums, expected_nums)

    def test_no_elements_to_remove(self):
        nums = [1, 2, 3, 4]
        val = 5
        expected_length = 4
        expected_nums = [1, 2, 3, 4]
        result = self.sol.removeElement(nums, val)
        self.assertEqual(result, expected_length)
        self.assertEqual(nums, expected_nums)

    def test_remove_all_elements(self):
        nums = [5, 5, 5, 5]
        val = 5
        expected_length = 0
        expected_nums = []
        result = self.sol.removeElement(nums, val)
        self.assertEqual(result, expected_length)
        self.assertEqual(nums, expected_nums)

    def test_single_element_array(self):
        nums = [6]
        val = 6
        expected_length = 0
        expected_nums = []
        result = self.sol.removeElement(nums, val)
        self.assertEqual(result, expected_length)
        self.assertEqual(nums, expected_nums)

    def test_large_array(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_length = 5
        expected_nums = [0, 1, 3, 0, 4]
        result = self.sol.removeElement(nums, val)
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:expected_length], expected_nums)

if __name__ == '__main__':
    unittest.main()