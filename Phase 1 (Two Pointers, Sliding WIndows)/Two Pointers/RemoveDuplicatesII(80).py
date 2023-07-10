class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #For the elements

        j, count = 1, 1

        for i in range(1, len(nums)):

            if nums[i - 1] == nums[i]:
                count += 1 #non unique element
            else:
                count = 1 #UNIQUE ELEMENT
            

            if count <= 2: #A duplicate element, but still not over the cap
                nums[j] = nums[i]
                j +=1
        
        return j