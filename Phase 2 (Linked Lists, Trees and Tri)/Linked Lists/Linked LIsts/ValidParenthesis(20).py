class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        mapping = {")": "(", "}": "{", "]": "["}


        #An edge case would be to ask if it's possible to have brackets other than the ones 
        #described in mapping.
        for char in s:

            #if closing bracket
            if char in mapping:
                #It is a closing bracket
                #check if the top element is of the same type
                temp = stack.pop() if stack else '#'

                #Above we considered the edge case of if the stack is empty
                
                if not mapping[char] == temp:
                    return False

            #It is an open bracket, so just push it onto the stack
            else:
                stack.append(char)
    
        #If stack is not empty, return false. Otherwise, return true

        return True if not stack else False