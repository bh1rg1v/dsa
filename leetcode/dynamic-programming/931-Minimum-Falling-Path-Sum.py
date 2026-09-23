class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        n = len(matrix)

        dp = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(n):

                if 0 <= j - 1 < n:
                    dp[i][j] = min(dp[i - 1][j - 1] + matrix[i][j], dp[i][j])

                if 0 <= j < n:
                    dp[i][j] = min(dp[i - 1][j] + matrix[i][j], dp[i][j])

                if 0 <= j + 1 < n:
                    dp[i][j] = min(dp[i - 1][j + 1] + matrix[i][j], dp[i][j])

        # for row in dp:
        #     print(row)

        return min(dp[-1])