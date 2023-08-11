class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:



        #Go through the lust

        i = 1
        while i < len(words):

            if sorted(words[i]) == sorted(words[i-1]):
                del words[i]
            else:
                i += 1
            
        return words