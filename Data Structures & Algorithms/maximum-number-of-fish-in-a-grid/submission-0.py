class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def bfs(row, col):
            queue = [(row, col)]
            total = 0
            while queue:
                row, col = queue.pop(0)
                total += grid[row][col]
                grid[row][col] = 0

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                        continue
                    
                    queue.append((r, c))
            
            return total
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    result = max(result, bfs(row, col))
        return result
