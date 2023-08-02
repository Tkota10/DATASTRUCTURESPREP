class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count = 0
        start = -1
        end = -1

        for i in range(len(nums)):
            if nums [i] > right:
                start = end = i #Reset the starting point
                continue
            if nums[i] >= left: #This is a valid point, 
                end = i
            
            count += end - start #since we know all the elements in here can form a valid subarray, we just do end - start. 

        return count
