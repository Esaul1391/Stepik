import pytest


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        max_dif = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_dif = max(max_dif, profit)
            else:
                l = r
            r += 1
        return max_dif


s = Solution()
sp = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(sp))


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