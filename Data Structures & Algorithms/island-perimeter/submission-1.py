class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:  
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            # if out of bounds or water return 1, 
            # meaning edge of the island.
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 1
            
            if grid[row][col] == 2: return 0
            
            # visited.
            grid[row][col] = 2
            _sum = 0
            
            # visit neigbors.
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                _sum += dfs(r, c)
            
            return _sum

        # traverse the array for 
        # the island starting point.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)