class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        def DFS(row, col):
            stack = [(row, col)]
            grid[row][col] = "0"
            while stack:
                curr_r, curr_c = stack.pop()
                if curr_r > 0 and grid[curr_r - 1][curr_c] == "1":
                    grid[curr_r - 1][curr_c] = "0"
                    stack.append((curr_r - 1, curr_c))
                if curr_c > 0 and grid[curr_r][curr_c - 1] == "1":
                    grid[curr_r][curr_c - 1] = "0"
                    stack.append((curr_r, curr_c - 1))
                if curr_r < len(grid) - 1 and grid[curr_r + 1][curr_c] == "1":
                    grid[curr_r + 1][curr_c] ="0"
                    stack.append((curr_r + 1, curr_c))
                if curr_c < len(grid[0]) - 1 and grid[curr_r][curr_c + 1] == "1":
                    grid[curr_r][curr_c + 1] = "0"
                    stack.append((curr_r, curr_c + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    DFS(r, c)
        
        return count
                
