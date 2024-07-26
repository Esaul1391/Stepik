class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = ''
        for i in s.lower():
            if i.isalnum():
                new += i

        ind_s = 0
        ind_e = len(new) - 1
        for _ in new:
            if new[ind_s] != new[ind_e]:
                return False
            ind_s += 1
            ind_e -= 1
        return True


s = Solution()
st = "A man, a plan, a cadnal: Panama"
print(s.isPalindrome(st))