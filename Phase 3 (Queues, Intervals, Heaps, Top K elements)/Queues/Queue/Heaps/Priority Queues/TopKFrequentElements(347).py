#Heap Solution, Very cool

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Calculate the counter or frequency
        freq_table = {}

        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1

        #Then create the heap, first do list comphrension, to make it into a max hheap
        heap = [(-freq, num) for num, freq in freq_table.items()]
        heapq.heapify(heap)
        
        # Get the k most frequent elements using nlargest function
        ans = [heapq.heappop(heap)[1] for _ in range(k)]

        return ans