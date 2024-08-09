class Solution:
    def numMagicSquaresInside(self, grid):
        def isMagicSquare(r, c):
            # Collect numbers in the 3x3 grid
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)

            # Check sums
            return (grid[r][c] + grid[r][c + 1] + grid[r][c + 2] == 15 and
                    grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] == 15 and
                    grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] == 15 and
                    grid[r][c] + grid[r + 1][c] + grid[r + 2][c] == 15 and
                    grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] == 15 and
                    grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] == 15 and
                    grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] == 15 and
                    grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2] == 15)

        count = 0
        rows, cols = len(grid), len(grid[0]) if grid else 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(i, j):
                    count += 1
        return count