class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_val = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        if init_val == color:
            return image
    
        def dfs(row, col):
            nonlocal init_val, color

            if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != init_val:
                return
            
            image[row][col] = color

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                dfs(r, c)

        
        dfs(sr, sc)

        return image