class Solution:
    def checkB(self,nums,mid,m,k):
        cnt=0
        n=0
        for i in nums:
            if i <= mid:
                cnt+=1
            else:
                n+=cnt//k
                cnt=0
        n+=(cnt//k)
        return n>=m
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        val=m*k
        if val>len(nums):
            return -1
        low=min(nums)
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.checkB(nums,mid,m,k):
                high=mid-1
                # ans=mid
            else:
                low=mid+1
        return low
        