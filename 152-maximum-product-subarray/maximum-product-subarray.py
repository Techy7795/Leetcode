class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        prod=1
        ma=float('-inf')
        for i in nums:
            prod*=i
            ma=max(ma,prod)
            if prod==0:
                prod=1
        prod=1
        for i in nums[::-1]:
            prod*=i
            ma=max(ma,prod)
            if prod==0:
                prod=1
        return ma



        