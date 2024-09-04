class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l1=len(word1)
        l2=len(word2)
        if l1<l2:
            for i in range(l1):
                res+=(word1[i]+word2[i])
            res+=word2[l1:]
        elif l2 < l1:
            for i in range(l2):
                res+=(word1[i]+word2[i])
            res+=word1[l2:]
        else:
            for i in range(l1):
                res+=word1[i]+word2[i]
        return res
        