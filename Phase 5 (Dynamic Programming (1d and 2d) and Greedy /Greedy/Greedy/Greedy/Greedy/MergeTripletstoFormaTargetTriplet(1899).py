class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        finalset = set()
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]: #Don't need to consider the triplets that are above the max
                continue
            for i, v in enumerate(trip):
                if v == target[i]:
                    finalset.add(i)

        return len(finalset) == 3
    
        #Important