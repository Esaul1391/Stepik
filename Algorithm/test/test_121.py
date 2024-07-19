import pytest
from Algorithm.a121 import Solution  # Предположим, что файл с вашим решением называется solution.py

def test_max_profit():
    solution = Solution()

    # Тестовый случай 1: обычный случай
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5

    # Тестовый случай 2: убывающие цены
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0

    # Тестовый случай 3: одномерный массив
    prices = [1]
    assert solution.maxProfit(prices) == 0

    # Тестовый случай 4: все цены одинаковые
    prices = [5, 5, 5, 5, 5]
    assert solution.maxProfit(prices) == 0

    # Тестовый случай 5: возрастающие цены
    prices = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices) == 4

    # Тестовый случай 6: две цены
    prices = [1, 2]
    assert solution.maxProfit(prices) == 1

if __name__ == "__main__":
    pytest.main()