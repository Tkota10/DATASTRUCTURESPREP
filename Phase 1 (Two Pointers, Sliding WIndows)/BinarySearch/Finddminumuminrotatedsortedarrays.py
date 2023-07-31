class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        #Binary Search

        #[4,5,6,7,0,1,2]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2


            ##if nums[mid] < nums[mid + 1]: #detection of our inflection point
                ##return nums[mid]


            
            if nums[mid] > nums[right]:  # Inflection point is in the right half.
                left = mid + 1
            else:  # Inflection point is in the left half or at mid.
                right = mid
        return nums[left]
        