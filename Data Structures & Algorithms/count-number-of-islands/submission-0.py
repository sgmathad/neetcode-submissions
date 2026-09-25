class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                dfs(r, c)
           
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        return islands