class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        
        intervals.sort(key = lambda x: x[0])
        prev = None
        for i in intervals:
            if prev is not None and prev[1] > i[0]:
                return False
            prev = i
        return True

        #The Time complexity would be NlogN, because the primary cause of this complexity is . Space complexity would be O(1), because no additional space is allocated