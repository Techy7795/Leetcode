class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int):
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        res=[]
        steps=1
        i=0
        total=0
        while total < rows * cols:
            for _ in range(2):
                dr,dc=directions[i]
                for j in range(steps):
                    if (0<=r<rows and 0<=c<cols):
                        res.append([r,c])
                        total+=1
                    r,c=r+dr,c+dc
                i=(i+1)%4
            steps+=1
        return res
