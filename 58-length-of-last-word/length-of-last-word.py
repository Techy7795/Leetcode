class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        c=0
        while i>=0:
            if s[i]==' ' and not c:
                i-=1
                continue
            elif s[i].isalpha():
                i-=1
                c+=1
            else:
                break
        return c
            
        

        