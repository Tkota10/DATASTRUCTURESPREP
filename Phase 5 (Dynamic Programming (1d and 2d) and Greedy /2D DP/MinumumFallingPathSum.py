class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """


        #DP SOLUTION

        #Add the current solution, plus the min to the end.

        #It's the min of a row though


        n = len(matrix)
        dp = [[0] * n for _ in range(n)] #Makes an array of all zeroes
        for i in range(n):
            dp[0][i] = matrix[0][i] #Initializes the first rows to just be the value of the grid
        
        for i in range(1, n): #This code block is essentially calculating thhe minumum value up to thhe previous value and then adding my value to it
            for j in range(n):
                current = dp[i - 1][j]
                if j - 1 >= 0:
                    current = min(current, dp[i - 1][j - 1])
                if j + 1 < n:
                    current = min(current, dp[i - 1][j + 1])
                dp[i][j] = current + matrix[i][j]
        return min(dp[-1]) #Whatever the smallest values is.