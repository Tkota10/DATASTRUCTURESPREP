class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #House Robbers #2
        def helper(num_lst):
            prev_max = 0
            curr_max = 0

            for num in num_lst:
                temp = curr_max
                curr_max = max(prev_max + num, curr_max)
                prev_max = temp

            return curr_max

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[1:]), helper(nums[:-1]))
            