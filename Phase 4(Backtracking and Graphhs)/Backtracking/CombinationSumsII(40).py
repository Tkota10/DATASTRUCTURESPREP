class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        candidates = sorted(candidates)

        def backtrack(remain, comb, start):
            if remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return
            else:
                prev = None
                for i in range(start, len(candidates)):  
                    if candidates[i] != prev: 
                        comb.append(candidates[i])
                        backtrack(remain-candidates[i], comb, i+1)
                        comb.pop()
                        prev = candidates[i]

        
        backtrack(target, [], 0)

        return res