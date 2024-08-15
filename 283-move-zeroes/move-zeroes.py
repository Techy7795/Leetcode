class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0
        for i in a:
            if i!=0:
                a[x]=i
                x+=1
        while x<len(a):
            a[x]=0
            x+=1