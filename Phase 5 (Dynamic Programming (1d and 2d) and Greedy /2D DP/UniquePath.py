class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        #Visited Set

        #Two Base cases

        #If we reach a corner


        #Reach our Target

        #Reach the bottom

        #Reach the right

        #Go left and right


        d = [[1] * n for _ in range(m)]

        for row in range(1,n):
            for col in range(1,m):
                d[col][row] = d[col-1][row] + d[col][row - 1]

        return d[m-1][n-1]