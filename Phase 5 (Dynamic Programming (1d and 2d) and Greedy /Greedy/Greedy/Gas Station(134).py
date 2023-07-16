class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        #if total gas is less than zero, than reset total. Start off withh a new index

        if sum(gas) < sum(cost):
            return -1

        total = 0
        
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost [i]

            if total < 0: #Greedy choice
                total = 0
                res = i + 1
                
        
        return res