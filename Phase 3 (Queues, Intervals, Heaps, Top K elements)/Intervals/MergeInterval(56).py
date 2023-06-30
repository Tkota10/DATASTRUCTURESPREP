class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda x: x[0])

        merged = []

        for interval in intervals:
            #if merged is empty or if the last element in merged is smaller than the first element in interval so you just include in the interval element
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
            
        
        return merged