class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        c=Counter(arr)
        for i in c:
            if c[i]==1 and k>0:
                k-=1
            if c[i]==1 and k==0:
                return i
        return ""
        