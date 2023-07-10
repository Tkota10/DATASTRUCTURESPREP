class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        res = []

        atl = set()
        pac = set()
        
        def dfs(i, j, visit, prevnode):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] < prevnode:
                return
            
            if (i, j) in visit:
                # already visited
                return
            
            visit.add((i, j))

            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])
        
        # Check the left or right elements

        1,2,3,4
        4,3,2,1
        1,3,2,4

        for j in range(len(heights[0])):
            dfs(0, j, pac, heights[0][j])
            dfs(len(heights) - 1, j, atl, heights[len(heights) - 1][j])
        
        # Check the top and bottom row
        for i in range(len(heights)):
            dfs(i, 0, pac, heights[i][0]) #Top Row
            dfs(i, len(heights[0]) - 1, atl, heights[i][len(heights[0]) - 1]) 
            #Bottom row
        return list(pac & atl)