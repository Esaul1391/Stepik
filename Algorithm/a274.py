class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        n = len(citations)

        for i in range(n):
            num_pubs = n - 1
            if citations[i] >= num_pubs:
                return num_pubs
        return 0


s = Solution()

ps = [3, 0, 6, 1, 5]

print(s.hIndex(ps))
