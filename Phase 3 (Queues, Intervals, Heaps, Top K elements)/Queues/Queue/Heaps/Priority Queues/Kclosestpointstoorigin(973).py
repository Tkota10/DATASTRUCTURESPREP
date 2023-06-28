class Solution(object):
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points: #grabs the first and second elements in each indices
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap) #This is the heap
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res
