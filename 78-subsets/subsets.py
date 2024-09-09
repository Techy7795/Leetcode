class Solution:
    def cons(self,index,nums,n,cur,ans):
        if index == n:
            ans.append(cur[:])
            return
        self.cons(index+1,nums,n,cur,ans)
        cur.append(nums[index])
        self.cons(index+1,nums,n,cur,ans)
        cur.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]
        self.cons(0,nums,len(nums),cur,ans)
        return ans
        