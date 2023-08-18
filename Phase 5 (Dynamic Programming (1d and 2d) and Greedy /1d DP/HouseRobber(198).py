class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        
        maximum_cost = [0] * n
        maximum_cost[0] = nums[0]
        maximum_cost[1] = max(nums[0], nums[1])

        for i in range(2, n):
            #Instead of just doing 'Maximum_cost[i-2] + nums[i], we also include the maximum_cost[i-1]
            maximum_cost[i] = max(nums[i] + maximum_cost[i-2], maximum_cost[i-1]) #rob either current house and combing with loot from two houses ago/ Otherwise, rob the combined loot from a house ago.
        return maximum_cost[-1]

