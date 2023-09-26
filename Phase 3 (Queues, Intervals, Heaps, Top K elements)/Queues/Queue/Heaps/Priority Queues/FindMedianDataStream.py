class MedianFinder:

    def __init__(self):
        self.minheap = [] #Second Hhalf
        self.maxheap = [] #First Half

    def addNum(self, num: int) -> None:

        #Have Two heaps representing the mid and Max Heap

        #Check if it's smaller than tap to f maxheap

        #Access Maxheap top

        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)


        while len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        while len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))


    def findMedian(self) -> float:

        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()