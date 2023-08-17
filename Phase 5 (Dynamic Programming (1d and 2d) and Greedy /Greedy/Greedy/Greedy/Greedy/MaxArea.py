class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        Greedy choice: Is the max area, greater than our current max area. If so, then we can change our values

        '''


        left = 0

        right = len(height) - 1
        area = 0

        while left < right:
            width = right - left

            area = max(area, min(height[right], height[left]) * width)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return area