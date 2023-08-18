class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        #Starting from the center and expanding outwards



        #We could use a queue; 

        for i in range(len(s)):

            #odd length

            l, r = i, i

            #Starting from thhe center (i) and then expanding outwards


            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r + 1] #This how you get the string from l to r
                    resLen = r - l + 1
                l -= 1
                r += 1 # Further expanding outwards

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r + 1] #This how you get the string from l to r
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
