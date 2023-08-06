class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """



        def findsquare(n):
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n = n // 10
            return temp
        
        slow = n
        fast = findsquare(n)

        while fast != 1:
            if slow == fast:
                return False
            slow = findsquare(slow)
            fast = findsquare(findsquare(fast))
        

        return True
