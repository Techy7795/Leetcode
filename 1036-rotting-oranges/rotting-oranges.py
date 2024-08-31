class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            rows, cols = len(grid), len(grid[0])
            queue = deque()
            fresh_oranges = 0
            
            # Step 1: Enqueue all initial rotten oranges and count fresh oranges
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        queue.append((r, c))
                    elif grid[r][c] == 1:
                        fresh_oranges += 1
            
            # Step 2: Perform BFS
            minutes = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while queue and fresh_oranges > 0:
                minutes += 1
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh_oranges -= 1
                            queue.append((nx, ny))
            
            # Step 3: Check if there are any fresh oranges left
            return minutes if fresh_oranges == 0 else -1
                