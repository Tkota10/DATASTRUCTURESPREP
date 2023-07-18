class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        #Count all the number of values of each number

        #For all the elements in hand.length,  run a for loop with groupsize being the iterator.


        countmap = {}

        #If it's not possible to get that far

        if len(hand) % groupSize != 0:
            return False

        #All the values in order

        for i in hand:
            countmap[i] = countmap.get(i, 0) + 1

        hand.sort()

        #now they are all in order

        for i in range(len(hand)):

            if countmap[hand[i]] == 0: #If there's no count left, leave it
                continue
            
            for j in range (groupSize):
                currcard = hand[i] + j #J Starts off at zero

                if countmap.get(currcard, 0) == 0: #If there's no element available. then call it off
                    return False

                countmap[currcard] -= 1
        

        return True