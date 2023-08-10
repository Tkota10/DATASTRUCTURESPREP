def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        10^3 = 111,222,333,444,555,666,777,888,999

        101, 103

        '''


        #9, 9, 8, 7, 6
        
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        count = 10  # for n = 1
        product = 9
        for i in range(2, n + 1):
            product *= (11 - i)
            count += product
        return count