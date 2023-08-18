class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        memo = [1] * len(nums)

        for i in range (len(nums)):
            for j in range(i): #checking all the elements before I
                if nums[i] > nums[j] and memo[i] < memo[j] + 1: 
                    #Nums[i] > nums[j] see if you can add an extra element; next condition says whichh is longest
                    memo[i] = memo[j] + 1
        
        return max(memo)