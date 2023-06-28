import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        self.heap = stones

        self.heap = [-x for x in self.heap]
        heapq.heapify(self.heap)
        while len(self.heap) > 1:
            y = heapq.heappop(self.heap)
            x = heapq.heappop(self.heap)
            if y != x:
                heapq.heappush(self.heap, -1 * ((-1 * y) - (-1 * x)))
        
        if not self.heap:
            return 0
        else:
            return (-1 *self.heap[0])