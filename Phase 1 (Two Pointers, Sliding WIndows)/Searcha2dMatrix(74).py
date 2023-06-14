class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        #Go through all the elements of the matrix
        #compare the target value to the last value of the element

        #Then check if it's bigger or less than the beginning or end values
        #Move Accordingly

        for i in range(len(matrix)):
            j = len(matrix[i]) - 1
            #Identify which of the rows is relevant
            if matrix[i][j] >= target and matrix[i][0] <= target:
                Temprow = matrix[i]
                right = j
                left = 0
                while left <= right:
                    midindex = (right + left)//2
                    if Temprow[midindex] > target:
                        right = midindex - 1
                    elif Temprow[midindex] < target:
                        left = midindex + 1
                    elif Temprow[midindex] == target:
                        return True
                return False
        return False