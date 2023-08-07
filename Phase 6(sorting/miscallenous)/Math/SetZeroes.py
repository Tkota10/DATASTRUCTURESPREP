class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """


        #Use the first row or first column to be zero

        dummyrow = [-1] * len(matrix)

        dummycol = [-1] * len(matrix[0])

        #Sets the columns and rows for where there is a zero

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dummyrow[i] = 0
                    dummycol[j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dummyrow[i] == 0 or dummycol[j] == 0:
                    matrix[i][j] = 0