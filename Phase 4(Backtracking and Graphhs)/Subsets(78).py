class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(curr_set, start):
            res.append(curr_set[:])
            for i in range(start, len(nums)):
                curr_set.append(nums[i])
                backtrack(curr_set, i + 1)
                curr_set.pop()

        backtrack([], 0)
        return res
