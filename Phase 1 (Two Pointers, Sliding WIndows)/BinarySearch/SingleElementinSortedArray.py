class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i+j) // 2
            if m < j and nums[m] == nums[m+1]:
                m = m + 1
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif abs(m-i) % 2 == 0:
                j = m - 1
            else:
                i = m + 1 
        return nums[i]