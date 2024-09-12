class Solution:
    def strStr(self, h: str, n: str) -> int:
        hlen=len(h)
        nlen=len(n)
        for i in range((hlen-nlen)+1):
            if h[i:i+nlen]==n:
                return i
        return -1
        