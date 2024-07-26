import pytest
from Algorithm.a392 import Solution

sol = Solution()

def test_is_subsequence():
    assert sol.isSubsequence("abc", "ahbgdc") == True
    assert sol.isSubsequence("axc", "ahbgdc") == False
    assert sol.isSubsequence("", "ahbgdc") == True
    assert sol.isSubsequence("abc", "") == False
    assert sol.isSubsequence("abc", "abc") == True
    assert sol.isSubsequence("", "") == True
    assert sol.isSubsequence("ace", "abcde") == True
    assert sol.isSubsequence("aec", "abcde") == False
