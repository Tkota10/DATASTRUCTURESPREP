class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        #Depth First Search algorothim


        def backtrack(remain, comb, start):
            #If you reach an element, that adds up to the target element, add that combination to the list. We use list(comb), because if we just append comb it'd be a pointer to a comb and that could change as we change aroudnd
            if remain == 0:
                res.append(list(comb))
                return
            #if you go past the cap, then end the search
            elif remain < 0:
                return
            #for all the elements in the list
            for i in range(start, len(candidates)):
                #add an element to existing combination
                comb.append(candidates[i])
                #Essentially running the function to see if it meets the condition
                backtrack(remain-candidates[i], comb, i)
                #Once it fails a condition or meets the condition, go back one to search for more.
                comb.pop()
            
        #Starts the search
        backtrack(target, [], 0)

        return res