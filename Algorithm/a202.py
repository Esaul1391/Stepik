class Solution(object):
    def isHappy(self, n):
        dict_sum_root = set()

        while n not in dict_sum_root:
            dict_sum_root.add(n)
            n = self.sumSquares(n)

            if n == 1:
                return True
        return False

    def sumSquares(self, n):
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output