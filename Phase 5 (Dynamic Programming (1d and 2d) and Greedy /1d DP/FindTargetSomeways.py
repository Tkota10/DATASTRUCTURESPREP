class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        '''
        5 Steps to solve a DP Problem:

        Type of problem: Knapsack problem

        States: Index where we are in the nums array
                Current Sum: All thhe current sums we've ingested. we want current sum to equal target sum

        Decision: Should we add the positive or negative value to our currentsum in hopes of getting our target sum
        '''

        memo = {}  # Memoization table

        def dp(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            if index < 0:
                if curr_sum == target:
                    return 1
                return 0

            positive = dp(index - 1, curr_sum + nums[index])
            negative = dp(index - 1, curr_sum - nums[index])

            memo[(index, curr_sum)] = positive + negative
            return memo[(index, curr_sum)]

        index = len(nums) - 1
        return dp(index, 0)