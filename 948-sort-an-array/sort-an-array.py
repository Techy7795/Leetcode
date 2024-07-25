class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        l=[]
        for i in sorted((set(nums))):
            for j in range(c[i]):
                l.append(i)
        return l
            


        