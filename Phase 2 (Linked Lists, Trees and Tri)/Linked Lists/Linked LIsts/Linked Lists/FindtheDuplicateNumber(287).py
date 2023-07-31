class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        #We know there is a repated number

        slow = 0
        fast = 0

        while True: # We know there is a cycle, and then we mark off one of the points as being in it. Not necceasrily the duplicat element but a point
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while fast != slow: #Find the cycle entrance
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow 