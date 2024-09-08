class Solution:
    def ispossible(self,nums,mid,m):
        cnt=1
        last=nums[0]
        for i in nums[1:]:
            if i-last >= mid:
                cnt+=1
                last=i
            else:
                continue
            if cnt==m:
                return True
        return False
        
    def maxDistance(self, nums: List[int], m: int) -> int:
        nums.sort()
        low=1
        high=max(nums)-min(nums)
        while low<=high:
            mid=(low+high)//2
            if not self.ispossible(nums,mid,m):
                high=mid-1
            else:
                low=mid+1
        return high

        