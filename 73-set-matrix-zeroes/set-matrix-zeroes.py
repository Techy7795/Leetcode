class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[0]*len(m)
        col=[0]*len(m[0])
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(len(m)):
            for j in range(len(m[0])):
                if row[i] or col[j]:
                    m[i][j]=0
