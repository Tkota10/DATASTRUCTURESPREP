#more efficient binary search problem

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Binary Search 
        i = 0

        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [(i+1), (j + 1)]
            if numbers[i] + numbers[j] > target: #Too big, increase the end value, so it can be closer to target
                j -= 1
            else:
                i += 1 #too small, need to get closer to target
        return []
