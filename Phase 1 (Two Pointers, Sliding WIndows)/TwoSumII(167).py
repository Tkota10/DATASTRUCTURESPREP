class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_maps = {}
        for i in range(len(numbers)):
            opposite = target - numbers[i]
            if opposite in num_maps:
                return [num_maps[opposite], i + 1]
            num_maps[numbers[i]] = i + 1
        return []