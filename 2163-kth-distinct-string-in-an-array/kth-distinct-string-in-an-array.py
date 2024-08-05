class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        c=Counter(arr)
        k1=1
        for i in c:
            if c[i]==1:
                if k1==k:
                    return i
                else:
                    k1+=1
        else:
         return ""
        