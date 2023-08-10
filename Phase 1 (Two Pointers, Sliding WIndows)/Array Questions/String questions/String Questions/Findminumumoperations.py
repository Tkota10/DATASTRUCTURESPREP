class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #All the nonpositive integers


        #Count all the non positive integeres

        count = 0

        numscount = {}

        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] not in numscount:
                    numscount[nums[i]] = 1
                
        
        return len(numscount)