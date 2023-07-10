class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return 1

        start = 0
        end = 1
        num = 0

        while end < n:
            diff = nums[end] - nums[start]

            if diff >= -target and diff <= target:
                start = end
                if end == n - 1:
                    num += 1
                    return num
                end += 1
                num += 1
            else:
                end += 1

        return -1