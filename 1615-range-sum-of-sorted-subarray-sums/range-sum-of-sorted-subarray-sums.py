class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod=(10**9)+7
        sub=[]
        for i in range(n):
            cur_sum=0
            for j in range(i,n):
                cur_sum=(cur_sum+nums[j])%mod
                sub.append(cur_sum)
        sub.sort()
        return sum(sub[left-1:right])%mod