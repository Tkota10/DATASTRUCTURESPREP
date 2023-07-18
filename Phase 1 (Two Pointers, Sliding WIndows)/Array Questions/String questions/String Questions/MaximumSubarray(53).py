class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsub = nums[0]

        itr = 0

        currsum = 0

        while itr < len(nums):
            if currsum < 0:
                currsum=0
            currsum += nums[itr]
            maxsub = max(maxsub, currsum)
            itr+=1
        return maxsub
 