class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_maps = {}
        for i in range(len(nums)):
            opposite = target - nums[i]
            if opposite in num_maps:
                return [num_maps[opposite], i]
            num_maps[nums[i]] = i
        return []

