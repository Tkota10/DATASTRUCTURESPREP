#Most efficient Solution


        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

            




#My original Solution

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #Insert elements into 
        #Negatize the elements
        #Pop the k elements
        #return negative of the biggest element

        self.heap = nums
        self.heap = [-x for x in self.heap]
        heapq.heapify(self.heap)

        while k > 1:
            heapq.heappop(self.heap)
            
            k -= 1
            

        return (-1 * heapq.heappop(self.heap))