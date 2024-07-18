class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)==1:
            return False
        def isDivisor(l):
            len1=len(s)
            if len1%l:
                return False
            f1=len1//l
            return s[:l]*f1==s
        for i in range(len(s)//2,0,-1):
            if isDivisor(i):
                return True
        return False


