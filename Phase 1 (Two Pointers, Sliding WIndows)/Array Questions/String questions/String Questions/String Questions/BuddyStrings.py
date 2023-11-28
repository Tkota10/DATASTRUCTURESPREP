class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        #Swap two letters, to equal string

        #if lengthh of s and length of goal aren't equal, return false. if s == goal, but none of the characters in S occur more than once, return False. Else return ture.


        if len(s) != len(goal):
            return False
    
        if s == goal:
            char_count = Counter(s)
            # Check if there's any character that occurs more than once
            return any(count >= 2 for count in char_count.values())

        diff = []
        # Find the positions where s and goal differ
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # Ensure there are exactly two differences and they can be swapped to make s and goal equal
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
                   