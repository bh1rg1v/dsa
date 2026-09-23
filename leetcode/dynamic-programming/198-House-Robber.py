class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)

        if n == 1: return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(2, n):
            dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1])

        return dp[-1]