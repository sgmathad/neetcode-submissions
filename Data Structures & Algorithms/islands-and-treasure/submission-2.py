class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        INF = 2147483647

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
        
        while queue:
            row, col, total = queue.pop(0)

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != INF or grid[r][c] == -1:
                    continue
                
                grid[r][c] = total + 1

                queue.append((r, c, total + 1))
                
