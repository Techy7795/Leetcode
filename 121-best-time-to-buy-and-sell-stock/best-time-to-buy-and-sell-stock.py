class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma=0
        mi=float('inf')
        for i in range(len(prices)):
            mi=min(mi,prices[i])
            ma=max(ma,prices[i]-mi)
        return ma