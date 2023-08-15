class Solution:
    def minFlips(self, target: str) -> int:

        #If you assume you start with zeroes, you can calculate the number of shifts from zero to 1

    
        count = 0


        prev = '0'


        for i in range(len(target)):

            if target[i] != prev:
                count += 1
            
            prev = target[i]
        
        return count