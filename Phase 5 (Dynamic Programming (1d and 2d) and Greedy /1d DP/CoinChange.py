class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        

    
    #Start off with a big number. And thhen we find theh min number of coins we need. This can be done all the way to the end index.


    #Main consideration: dp[a] = min(dp[a], 1 + dp[a - c]). "This Dp[A-C] is seeing what would we happen if we added that coin, what would be the min value. If our value is 9, and our coin is 5, we take what we have from value 4 and add 1 (to get to 9)"


    #if a - c >= 0:

        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1