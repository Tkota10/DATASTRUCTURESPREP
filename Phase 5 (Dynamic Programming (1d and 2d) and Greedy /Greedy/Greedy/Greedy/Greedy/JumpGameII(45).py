class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Set the last element to be a target:


        #Then start from the beginning and then once you find an element, you use thhe hashtable to see what element reaches. And then continue to do the hashtable until you find your element.


        res = 0

        cur = far  = 0

        while far < len(nums) -1: #If you go past this element, than you have to return the value you have right now
            farthest = 0
            for i in range(cur, far + 1): # Seeing the element in the specified segment
                farthest = max(farthest, i + nums[i])
            cur = far + 1
            far = farthest
            res += 1
        
        return res
        