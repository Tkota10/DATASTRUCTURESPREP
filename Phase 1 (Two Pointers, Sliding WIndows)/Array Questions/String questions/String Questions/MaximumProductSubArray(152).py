##Correct Solution:

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #set it some arbitrary value
        maxproduct = max(nums)

        #Calculate because if you have an odd number of negative number, it's possi
        #ble you have the max if you
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tmp = curMax * n
            curMax = max(n * curMax, n *curMin, n)
            curMin = min(tmp, n * curMin, n)
            maxproduct = max(maxproduct, curMax)
        return maxproduct


#My Solution (passed some test cases)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxproduct = nums[0]

        tempmax = nums[0]

        for index, value in enumerate(nums):
            if index >= 1:
                tempmax *= value
                maxproduct = max(tempmax, maxproduct)
        return maxproduct