class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        index_map = {}

        #Stores all the indexes

        for index, char in enumerate(s):
            index_map[char] = index

       #We know have the last occurence

        res = []
        start = 0
        end = 0
        for index, char in enumerate(s):
           end = max(end, index_map[char])

           if index == end:
               res.append(end - start + 1)
               start = index + 1
            
        
        return res



'''
Approach: Find all the max occurences. Then iterate through the array and keep track of the max occurence of the index. When index equals max occurences, than that's a partition.

'''