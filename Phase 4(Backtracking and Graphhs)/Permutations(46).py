class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #combingation

        res = []

        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(list(comb))
                return
            for i in range(len(nums)):
                if nums[i] not in comb:
                    comb.append(nums[i])
                    backtrack(comb)
                    comb.pop()
            
        
        backtrack([])

        return res