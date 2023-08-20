lass Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''

        Store a hashmap with the number of distinct characters

        #Then have a maxlen variable increase until we get three distinct values in the hashmap

        '''



        count = Counter()
        left = 0
        right = 0
        maxlen = 0
        
        while right < len(s):
            count[s[right]] += 1
            
            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            
            maxlen = max(maxlen, right - left + 1)
            
            right += 1
        
        return maxlen