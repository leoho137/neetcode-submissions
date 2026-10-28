class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        def DFS(row, col):
            area = 0
            stack = [(row, col)]
            grid[row][col] = 0
            while stack:
                curr_r, curr_c = stack.pop()
                area += 1
                if curr_r > 0 and grid[curr_r - 1][curr_c] == 1:
                    grid[curr_r - 1][curr_c] = 0
                    stack.append((curr_r - 1, curr_c))
                if curr_c > 0 and grid[curr_r][curr_c - 1] == 1:
                    grid[curr_r][curr_c - 1] = 0
                    stack.append((curr_r, curr_c - 1))
                if curr_r < len(grid) - 1 and grid[curr_r + 1][curr_c] == 1:
                    grid[curr_r + 1][curr_c] = 0 
                    stack.append((curr_r + 1, curr_c))
                if curr_c < len(grid[0]) - 1 and grid[curr_r][curr_c + 1] == 1:
                    grid[curr_r][curr_c + 1] = 0
                    stack.append((curr_r, curr_c + 1))
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(DFS(r, c), maxArea)
        return maxArea


