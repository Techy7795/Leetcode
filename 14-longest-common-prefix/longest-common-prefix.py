class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        start=0
        res=""
        for char in strs[0]:
            if char==strs[-1][start]:
                res+=char
                start+=1
            else:
                return res
        return res
        