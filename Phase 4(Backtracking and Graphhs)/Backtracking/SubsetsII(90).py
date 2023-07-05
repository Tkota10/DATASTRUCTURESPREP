#my Initial solution

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)


        def backtrack(curr_set, start):
            if curr_set[:] not in res:
                res.append(curr_set[:])
            for i in range(start, len(nums)):
                curr_set.append(nums[i])
                backtrack(curr_set, i + 1)
                curr_set.pop()

        backtrack([], 0)
        return res




#Best Solution:

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]] 1, 3, 3, 4
        """
        res = []
        nums = sorted(nums)

        def backtrack(curr_set, start):
            res.append(curr_set[:])  # Always append the current subset
            prev = None  # Track the previously chosen element
#[2,2]. [2] prev = 2
            for i in range(start, len(nums)):
                if nums[i] != prev:
                    curr_set.append(nums[i])
                    backtrack(curr_set, i + 1)
                    curr_set.pop()
                    prev = nums[i]

        backtrack([], 0)
        return res