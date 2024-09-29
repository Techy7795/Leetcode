class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        c=Counter(nums)
        sum=0
        for i in c:
            if c[i]==1:
                sum+=i
        return sum
        