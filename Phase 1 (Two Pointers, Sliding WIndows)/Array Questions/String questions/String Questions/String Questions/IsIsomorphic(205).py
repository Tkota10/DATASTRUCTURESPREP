class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_map = {}  # Renamed from 'map' to 's_map'
        t_map = {}  # Renamed from 'map' to 't_map'

        itr = 0

        while itr < len(s):
            if s[itr] in s_map: #If s has already been stored
                if s_map[s[itr]] != t[itr]: #if the t element does not match the current element, then it's false
                    return False
            elif t[itr] in t_map:#since the s_map element and t_map element are being added together, if the t_map element is found that means that the t_map element doesn't match with the s_element (reverse)
                return False
            else:
                s_map[s[itr]] = t[itr]
                t_map[t[itr]] = s[itr]
            itr += 1
        
        return True