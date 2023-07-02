class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: x[0])
        overlapping = 0
        prev = intervals[0]
        
        for i in intervals[1:]:
            if i[0] < prev[1]:
                overlapping += 1
                if i[1] < prev[1]:
                    prev = i
            else:
                prev = i
    
        return overlapping
