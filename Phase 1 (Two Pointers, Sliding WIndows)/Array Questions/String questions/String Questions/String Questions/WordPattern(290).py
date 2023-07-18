class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split()  # Split the string into words

        if len(words) != len(pattern):
            return False

        wordmap = {}
        patternmap = {}

        itr = 0

        while itr < len(words):
            if pattern[itr] in wordmap:
                if wordmap[pattern[itr]] != words[itr]:
                    return False
            elif words[itr] in patternmap:
                return False
            else:
                wordmap[pattern[itr]] = words[itr]
                patternmap[words[itr]] = pattern[itr]
            itr += 1

        return True