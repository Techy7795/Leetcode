class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans, count = 0, 0
        for i in s:
            if i == '1':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans

        acr=0
        for i in s:
            acr+=1 if i=="0" else 0
        bcl=0
        res=len(s)
        for c in s:
            if c=="0":
                acr-=1
            res=min(res,acr+bcl)
            if c=="1":
                bcl+=1 
        return res
        