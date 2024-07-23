class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            row=min(matrix[i])
            cindex=matrix[i].index(row)
            col = max(matrix[j][cindex] for j in range(len(matrix)))
            if row==col:
                return [row]
        