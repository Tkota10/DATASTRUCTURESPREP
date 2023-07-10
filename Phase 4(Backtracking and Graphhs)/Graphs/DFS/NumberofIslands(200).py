#The time complexity is O(M*N) because you visit all the elements the 


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        gridelem = grid #NOT NEEDED DUMBASS (Because it's a reference not a deepcopy)

        num = 0 #nmr of islands

        if not gridelem:
            return 0

        
        def dfs(grid, i, j):
            #Whenever I get to a 1, I continue, whenever I get to a zero, I stop my dFS

            #Identifying elements that would considered water 
            if i < 0 or i >= len(gridelem) or j < 0 or j >= len(gridelem[0]) or gridelem[i][j] != '1':
                return
            
            gridelem[i][j] = '#'

            dfs(gridelem, i + 1, j)
            dfs(gridelem, i - 1, j)
            dfs(gridelem, i, j - 1)
            dfs(gridelem, i, j + 1)
        #Iterate through grid

        for i in range(len(gridelem)):
            for j in range(len(gridelem[0])):
                if gridelem[i][j] == '1':
                    num +=1
                    dfs(gridelem, i, j)
        
        
        
        return num
