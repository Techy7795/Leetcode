class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1 or len(s)<=n:
            return s
        res=['']*n
        rows=0
        down=False

        for c in s:
            res[rows]+=c
            if rows==0 or rows==n-1:
                down=not down
            rows+= 1 if down else -1
        return ''.join(res)

        