class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #Two pointers method

        '''Essentialy, we used two pointers to compare both of the indices 
        of the strings in order, depending on the element order of element 
        s(which is good). If i is equal to the len(s), this is good because
          this means all the elements have been found '''

        if not s:
            return True

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
