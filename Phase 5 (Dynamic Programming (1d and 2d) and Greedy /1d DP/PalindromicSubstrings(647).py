class Solution(object):
    def countSubstrings(self, s):
        

        count = 0



        for i in range(len(s)):

            #Odd palindrome
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
            
                l -= 1
                r += 1

            
            #Even palindrome: such as 'aa'

            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
            
                l -= 1
                r += 1
        
        return count
