class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #combingation

        res = []

        def backtrack(comb):
            #Once I get 4 Numbers, I return
            if len(comb) == len(nums):
                res.append(list(comb))
                return
            #DFS
            for i in range(len(nums)):
                if nums[i] not in comb:
                    comb.append(nums[i])
                    backtrack(comb)
                    comb.pop()
            
        
        backtrack([])

        return res