class Solution(object):
    def climbStairs(self, n):

        memo = {}

        def dfs(n):
            if n <= 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)
