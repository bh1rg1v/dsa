class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        ans = 0
        n = len(prices)

        minSoFar = prices[0]

        for i in range(1, n):
            val = prices[i] - minSoFar
            ans = max(ans, val)
            minSoFar = min(minSoFar, prices[i]) 

        return ans