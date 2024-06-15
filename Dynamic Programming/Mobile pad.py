# Examples

# Input: n = 1
# Output: 10
# Explanation: Number of possible numbers are 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  
# Input: n = 2
# Output: 36
# Explanation: Possible numbers: 00, 08, 11, 12, 14, 22, 21, 23, 25 and so on. If we start with 0, valid numbers will be 00, 08 (count: 2). If we start with 1, valid numbers will be 11, 12, 14 (count: 3). If we start with 2, valid numbers  will be 22, 21, 23,25 (count: 4). If we start with 3, valid numbers will be 33, 32, 36 (count: 3). If we start with 4, valid numbers will be 44,41,45,47 (count: 4). If we start with 5, valid numbers will be 55,54,52,56,58 (count: 5) and so on.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

class Solution:
	def getCount(self, N):
		# code here
		dp = [[0] * 10 for _ in range(N + 1)]
 
        data = [[0, 8], [1, 2, 4], [1, 2, 3, 5], [2, 3, 6], 
            [1, 4, 5, 7], [2, 4, 5, 6, 8], [3, 5, 6, 9], 
            [4, 7, 8], [5, 7, 8, 9, 0], [6, 8, 9]]
 
        for i in range(1, N + 1):
            for j in range(10):
                if i == 1:
                    dp[i][j] = 1
                else:
                    for prev in data[j]:
                        dp[i][j] += dp[i - 1][prev]
 
        sum = 0
        for j in range(10):
           sum += dp[N][j]
 
        return sum
