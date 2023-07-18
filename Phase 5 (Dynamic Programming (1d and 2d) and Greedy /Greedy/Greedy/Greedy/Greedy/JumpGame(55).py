class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #for loop

        #Add the loop

        #Start from thhe end of the array

        target = len(nums) - 1

        for i in range (len(nums) - 2, -1, -1): #Starting from the last element and go down
            if (i + nums[i]) >= target:
                target = i





        return target == 0