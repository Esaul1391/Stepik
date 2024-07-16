import pytest
from Algorithm.a169 import Solution


def test_majority_element():
    solution = Solution()

    # Тестовый случай 1: обычный случай
    assert solution.majorityElement([3, 2, 3]) == 3

    # Тестовый случай 2: элемент явно является большинством
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

    # Тестовый случай 3: один элемент
    assert solution.majorityElement([1]) == 1

    # Тестовый случай 4: два одинаковых элемента
    assert solution.majorityElement([1, 1]) == 1

    # Тестовый случай 5: большие данные
    assert solution.majorityElement([5] * 5000 + [6] * 4999) == 5

    # Тестовый случай 6: равное количество разных элементов (не может произойти по условиям задачи, но тестируем)
    # with pytest.raises(Exception):
    #     solution.majorityElement([1, 2, 3, 4, 5, 6])
