class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        '''

        Constraints:

        1) has to run in O(N) run time

        2) length of longest consecutive elemenets sequence


        Approach:

        Put elements in a set (So we can have O(1) lookup

        For any element where the predecessor is not in the map, then we can count how many consecutive elements.


        '''


        longest_consec = 0

        nums = set(nums)

        for num in nums:

            if num - 1 not in nums: #no previous element in the set
                templen = 1 #the initial length is 1
                tempnum = num
                while tempnum + 1 in nums:
                    templen += 1
                    tempnum = tempnum + 1
            
                longest_consec = max(longest_consec, templen)
        
        return longest_consec