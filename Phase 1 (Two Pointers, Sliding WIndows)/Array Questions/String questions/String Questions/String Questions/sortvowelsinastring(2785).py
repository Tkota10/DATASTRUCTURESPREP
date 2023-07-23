class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = []

        for char in s:
            if char in "aeiouAEIOU":
                vowels.append(char)
        vowels.sort()

        retval = ""
        for char in s:
            if char in "aeiouAEIOU":
                retval += vowels.pop(0)
            else:
                retval += char

        return retval