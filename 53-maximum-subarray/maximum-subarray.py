class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        su=0
        maxi=float('-inf')
        for i in range(len(a)):
            su+=a[i]
            if su>maxi:
                maxi=su
            if su<0:
                su=0
        return maxi
                

        