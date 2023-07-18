class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """


        #Go thhrough the list and th

        anagram_map = {}

        for word in strs:
            sorted_chars = sorted(word)
            sorted_str = ''.join(sorted_chars)
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(word)  # Append the word to the existing list
            else:
                anagram_map[sorted_str] = [word]
            
        return list(anagram_map.values())