class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def memo_solve(p1, p2):

            #If it's in memo, return that value
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0

            #Recursive Case #1 (Both of the letters are the same)
            
            if text1[p1] == text2[p2]:
                result = 1 + memo_solve(p1 + 1, p2 + 1)
           
            #Recursive Case #2 (Not the same, so now we explore one step further in either the left or right side): Return the max value
            else:
                result = max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
            
            memo[(p1, p2)] = result
            return result
                
        return memo_solve(0, 0)



        '''
        Subproblem I'm trying to solve:

        #If we include 