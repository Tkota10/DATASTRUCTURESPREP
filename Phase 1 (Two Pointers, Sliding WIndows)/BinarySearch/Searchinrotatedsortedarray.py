class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        '''
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
        '''
        


        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: #Inflection point is on the righht
                if target >= nums[left] and target < nums[mid]: #checks if the target is in the left quadrant (because we know if the first condition is true, everything is going upwards)
                    right = mid
                else:
                    left = mid + 1

            else: #Inflection point is on the left
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

            
        
        return -1