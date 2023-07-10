#Efficient solution

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        prev = nums[0]  # Track the previous element
        unique_idx = 1  # Index to store the next unique element

        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[unique_idx] = nums[i]  # Store the unique element at the next unique index
                prev = nums[i]  # Update the previous element
                unique_idx += 1  # Increment the unique index
        
        return unique_idx
                

#My solution

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = None

        num = 0
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
                
            else:
                prev = nums[i]
                num += 1
                i += 1
        
        return num