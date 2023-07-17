class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #Go through each column
        nums.sort()
        i = 0
        #sliding windown technique
        '''
        [4, 6, 1, 2]

        [1, 2 , 4, 6] i = 0

        [1, 2(j), 4, 6] i = 0
        
        [1, 2, 4(j), 6] i = 0

        [1, 2, 4, 6 (j)] i = 1
O(nlogn) = 


        '''
        
        for j in range(len(nums)):
            if nums[j] - nums[i] > k * 2: #Trying to find the largest subsqequence that  passes the array
                i += 1 #test a new subsequence

        return j - i + 1
    



class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #Go through each column
        max_beauty = 0
        Count_map = {}

        for num in nums:
            # 
            Count_map[num] = Count_map.get(num, 0) + 1

            # Go through all the values that are possible for the replacement range
            for replacement in range(num - k, num + k + 1):
                # Update max_beauty withh what's bigger, max_beauty or the replacement value
                if replacement in Count_map:
                    if not replacement == num:
                        Count_map[replacement] += 1
                    max_beauty = max(max_beauty, Count_map[replacement])

        return max_beauty
