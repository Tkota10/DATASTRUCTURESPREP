class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #Can't use the division operation

        #Calculate the left product

        #Calculate the right product


        res = [1] * (len(nums))

        prefix = 1 #Left side

        for i in range(len(nums)): #Iterate and add the base values
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 #Right side
        for j in range(len(nums) - 1, -1, -1): #Go through and do the accesory values
            res[j] *= postfix
            postfix *= nums[j]
        return res
