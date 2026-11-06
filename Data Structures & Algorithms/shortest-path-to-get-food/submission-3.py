class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(row, col):
            queue = [(row, col, 0)]
            grid[row][col] = 'X'
            while queue:
                row, col, total = queue.pop(0)

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'X':
                        continue
                    if grid[r][c] == '#':
                        return total + 1
                    grid[r][c] = 'X'
                    queue.append((r, c, total + 1))
            
            return -1
                

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    return bfs(row, col)