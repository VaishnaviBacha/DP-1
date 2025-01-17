# Time Complexity: O(m * n) where m => number of coins, n => amount
# Space Complexity: O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, len(coins)+1):
            for j in range(0, amount+1):
                if j >= coins[i-1]:
                    dp[j] = min(dp[j], dp[j-coins[i-1]] + 1)
        if dp[amount] == float('inf'):
            return -1
        return int(dp[amount])