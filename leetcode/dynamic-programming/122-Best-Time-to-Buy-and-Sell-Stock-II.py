class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        
        ans = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                ans += nums[i] - nums[i - 1]

        return ans