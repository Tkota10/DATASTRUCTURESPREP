class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        #valid or invalid state

        #valid (one or fewer 0's)
        
        #invalid sate (two 0's in our current sequence)

        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):
            if nums[right] == 0: #if we've reach another zero, add to our total of 'num_zeroes'
                num_zeroes += 1
            
            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes -= 1 #reduce it back to 1, so now we're chhilling
                left += 1
            
            longest_sequence = max(longest_sequence, right - left + 1)

            right += 1
        
        return longest_sequence