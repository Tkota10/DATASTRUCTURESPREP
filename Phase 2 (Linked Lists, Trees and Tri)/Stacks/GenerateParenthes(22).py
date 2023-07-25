class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''



        Only add open paranthesis if the count of openN is less than n
        only add closed parenthis if count of closed parenthis is less than count of open paranthhesis
        Add to result if open == closed == n

        '''

        stack = []

        res = []

        def backtrack(openN, closedN):

            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() #it's a global variable, so once we're done doing our analysis, we have to get rid of it
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0 , 0)
            
        return res