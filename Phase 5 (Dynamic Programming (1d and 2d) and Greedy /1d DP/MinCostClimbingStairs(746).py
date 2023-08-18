class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        #cst variable to see what is better 

        #start a decision tree 



        minumum_cost = [0] * (len(cost) + 1) #Stores the array of all the minumum values

        #step 1 and zero

        for i in range(2, len(cost) + 1):
            Cst_1_step = minumum_cost[i - 1] + cost[i - 1] #what the cost would be if you do a jump of 
            Cst_2_step = minumum_cost[i - 2] + cost[i -2 ] #what the cost would be if you do a jump of 
            minumum_cost[i] = min(Cst_1_step, Cst_2_step ) #Now store what the minumum value is at that point. Thus, all the possible values for Min_value can only be from there. This gets rid of a lot of possibilities
        return minumum_cost[-1] #The last value is the most important value
    

    [1,2,3,4,5]
    

    [0,0,2, 2]