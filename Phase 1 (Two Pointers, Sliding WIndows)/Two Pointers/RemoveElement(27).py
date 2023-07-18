class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        #If i see a bad value, ignore it and continue to drop it

        g = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[g] = nums[i]
                g += 1
        
        return g