class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        n = max(nums)
        if len(nums) != n + 1:
            return False

        num_set = set()
        count_n = 0

        for num in nums:
            if num == n:
                count_n += 1
            elif num in num_set:
                return False
            else:
                num_set.add(num)

            

        return count_n == 2