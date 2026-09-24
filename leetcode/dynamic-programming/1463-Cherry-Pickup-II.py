class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        
        @lru_cache(maxsize=None)
        def dp(r, c1, c2):

            if r == m: return 0

            ans = 0

            for i in range(-1, 2):
                for j in range(-1, 2):

                    nc1 = c1 + i
                    nc2 = c2 + j

                    if 0 <= nc1 < n and 0 <= nc2 < n:
                        ans = max(ans, dp(r + 1, nc1, nc2))

            if c1 == c2:
                cherries = grid[r][c1]
            else:
                cherries = grid[r][c1] + grid[r][c2]

            ans += cherries
            return ans

        ans = dp(0, 0, n - 1)
        dp.cache_clear()

        return ans