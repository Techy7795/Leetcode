class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * (n + 1) for _ in range(n)]
        dp[0][0] = True  # Starting point

        for i in range(n):
            for k in range(n):
                if dp[i][k]:
                    for jump in (k - 1, k, k + 1):
                        if jump > 0:
                            next_stone = stones[i] + jump
                            if next_stone in stones:
                                dp[stones.index(next_stone)][jump] = True

        return any(dp[n - 1])
        