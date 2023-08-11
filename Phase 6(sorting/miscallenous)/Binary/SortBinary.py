class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        for num in arr:
            ones = self.countBits(num)
            res.append((ones, num))
        heapq.heapify(res)
        finalres = []
        while len(res)>0:
            finalres.append(heappop(res)[1])
        return finalres
    
    def countBits(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
            n >>= 1
        return count