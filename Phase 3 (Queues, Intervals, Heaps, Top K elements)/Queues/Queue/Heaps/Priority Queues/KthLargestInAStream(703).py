import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.idx = k
        #Initialize a queue/Heap and add all the elements 
        """
        :type k: int
        :type nums: List[int]
        """
        self.arr = nums
        heapq.heapify(self.arr)

        while len(self.arr) > k:
            heapq.heappop(self.arr)
        
        #No only have k elements
        

    def add(self, val):
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.idx:
            heapq.heappop(self.arr)
       

        return self.arr[0]
        """
        :type val: int
        :rtype: int
        """