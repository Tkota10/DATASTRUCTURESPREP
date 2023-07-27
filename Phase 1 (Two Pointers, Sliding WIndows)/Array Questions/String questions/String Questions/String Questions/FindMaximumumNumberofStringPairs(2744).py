class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        

        word_dict = []

        count = 0
        
        for word in words:
            reversedstring = word[::-1]
            if reversedstring in word_dict:
                word_dict.remove(reversedstring)
                count += 1
            else:
                word_dict.append(word)
        
        return count