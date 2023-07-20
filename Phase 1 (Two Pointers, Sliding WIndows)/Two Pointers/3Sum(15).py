class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        #Go through the list with two pointers

        nums.sort()

        

        for i, a in enumerate(nums): #i is the index, a is the value
            #If i get the same value as the previous index/I don't want to repeat the value
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            
            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum == 0:
                    res.append([a, nums[l], nums[r]])
                    #keep on going through duplicates
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res