class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Bubble Sort Solution

        count = {}

        freq = [[] for i in range(len(nums) + 1)] #So we include the length too

        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        
        #Count now contains the frequence for each element

        for n, i in count.items(): #i is the count, n is the value
            freq[i].append(n)

        for j in range(len(freq) - 1, 0, -1):

            for n in freq[j]: #Add in all the possible elements you can
                res.append(n)
                if len(res) == k:
                    return res