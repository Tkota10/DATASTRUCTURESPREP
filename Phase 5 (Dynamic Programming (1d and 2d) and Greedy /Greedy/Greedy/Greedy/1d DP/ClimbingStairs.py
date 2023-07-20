class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #n is the target to go over
        #Start off with 0
        #two options add 1 or add 2
        #Res variable

        res = 0

        memo = [-1 for _ in range(n)]
        def explore(cur):
            if cur > n:
                return 0
            elif cur == n:
                return 1
            
            if memo[cur] != -1: #Memo so we never have to read it in again
                return memo[cur]
            
            memo[cur] = explore(cur + 1) + explore(cur + 2)
            return memo[cur]
        return explore(0)
            