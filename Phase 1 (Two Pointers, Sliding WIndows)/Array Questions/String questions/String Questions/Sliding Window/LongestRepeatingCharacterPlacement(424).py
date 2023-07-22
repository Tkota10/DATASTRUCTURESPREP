class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        #Two Pointers

        #Then you can iterate thhrough theh list

        count = {}

        left = 0


        str_length = 0

        for i in range(len(s)): #Right pointer
            if not s[i] in count:
                count[s[i]] = 0
            count[s[i]] += 1

            #This will add the frequency of the value. Which allows us to then return the max string length afterwards

        
            replacement = (i - left + 1) - max(count.values()) #Highest frequency item

            if replacement <= k: #We haven't gotten there yet, but we'll take the max length
                str_length = max(str_length, (i- left + 1))
            else:
                count[s[left]] -= 1 #Too big, and now we'll try a different lengthh/ To do that we get rid of the key first
                if not count[s[left]]:
                    count.pop(s[left]) #Get rid of the key
                left += 1 #Moves the index over, making it smaller
        return str_length
        