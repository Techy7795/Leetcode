class Solution:
    def minimumDeletions(self, s: str) -> int:
        acr=0
        for i in s:
            acr+=1 if i=="a" else 0
        bcl=0
        res=len(s)
        for c in s:
            if c=="a":
                acr-=1
            res=min(res,acr+bcl)
            if c=="b":
                bcl+=1 
        return res

        