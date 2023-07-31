class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxlen = 0
        for i in s:
            if len(i) > maxlen:
                maxlen = len(i)
        
        solution = [""] * maxlen #That's the max our array will have to be

        for word in s:
            for j in range(maxlen):
                if j < len(word):
                    solution[j] += word[j]
                else:
                    solution[j] += " " #We do this instead of 

        for j in range(len(solution)):
            solution[j] = solution[j].rstrip()
        

        return solution
    
        "How Are you doing"

        Solution = ["Hayd", "Oroo" , "Weui" , "n", "    g"]
        

            