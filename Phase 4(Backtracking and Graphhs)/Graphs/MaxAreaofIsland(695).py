class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        area = 0
        if not grid:
            return 0
        

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            cur_area = 1

            # Explore the neighboring cells
            cur_area += dfs(grid, i + 1, j)
            cur_area += dfs(grid, i - 1, j)
            cur_area += dfs(grid, i, j - 1)
            cur_area += dfs(grid, i, j + 1)

            return cur_area


        #Goes through the entire island, and whenever you reach a 1, you enter the DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    elem_area = dfs(grid, i, j)
                    area = max(area, elem_area)

        return area