class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total_sum = 0
        for i in range(k):
            total_sum += nums[i]
        
        average_sum = total_sum / k

        #This is the intial sum of all the values

        left = 0 #The first element of the subarray

        for i in range(k,len(nums)):
            total_sum = total_sum - nums[left] + nums[i]
            average_sum = max(average_sum, total_sum / k)
            left += 1

        return average_sum