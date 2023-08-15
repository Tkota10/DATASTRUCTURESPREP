class Solution:
    def winnerOfGame(self, colors: str) -> bool:


        #Find A

        #Find B


        #If thhe count of same letters in a row, is bigger than or equal to 3. Return n-2, for total you can remove

        countA = 0
        countB = 0

        for i in range(1, len(colors) - 1, 1):
            if colors[i] == 'A':
                if colors[i - 1] == 'A' and colors[i + 1] == 'A':  # Check neighbors
                    countA += 1
            elif colors[i] == 'B':
                if colors[i - 1] == 'B' and colors[i + 1] == 'B':  # Check neighbors
                    countB += 1
            
        
        return (countA > countB)
