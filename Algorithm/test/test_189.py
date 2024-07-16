import pytest
from Algorithm.a189 import Solution  # предположим, что файл с вашим решением называется solution.py

def test_rotate():
    solution = Solution()

    # Тестовый случай 1: обычный случай
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution.rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Тестовый случай 2: k больше длины массива
    nums = [-1, -100, 3, 99]
    k = 2
    solution.rotate(nums, k)
    assert nums == [3, 99, -1, -100]

    # Тестовый случай 3: k меньше длины массива
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    solution.rotate(nums, k)
    assert nums == [5, 6, 1, 2, 3, 4]

    # Тестовый случай 4: k равен длине массива
    nums = [1, 2, 3, 4, 5]
    k = 5
    solution.rotate(nums, k)
    assert nums == [1, 2, 3, 4, 5]

    # Тестовый случай 5: пустой массив
    nums = []
    k = 3
    solution.rotate(nums, k)
    assert nums == []

    # Тестовый случай 6: массив с одним элементом
    nums = [1]
    k = 0
    solution.rotate(nums, k)
    assert nums == [1]

    # Тестовый случай 7: массив с двумя элементами
    nums = [1, 2]
    k = 1
    solution.rotate(nums, k)
    assert nums == [2, 1]

if __name__ == "__main__":
    pytest.main()