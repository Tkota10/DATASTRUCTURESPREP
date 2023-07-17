from collections import Counter

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right, left = Counter(nums), Counter()
        n = len(nums)
        leftl, rightl = 0, n #left and right array length
         
        maxl, maxli = 0, 0 #left max occurance and its key
        
        for i, num in enumerate(nums):
            left[num] += 1
            right[num] -= 1
            leftl += 1
            rightl -= 1
            
            if left[num] > maxl:
                maxl = left[num]
                maxli = num
            
            if right[maxli] * 2 > rightl and maxl * 2 > leftl:
                return i
  
        return -1