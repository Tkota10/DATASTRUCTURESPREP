class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        p_count = [0] * 26  # Using a fixed-size array to count occurrences of characters in 'p'
        s_count = [0] * 26
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return res

        # Count occurrences of characters in 'p'
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        # Count occurrences of characters in the first window
        for i in range(len_p):
            s_count[ord(s[i]) - ord('a')] += 1

        # Check the first window for an anagram
        if p_count == s_count:
            res.append(0)

        # Sliding window through the string 's'
        for i in range(1, len_s - len_p + 1):
            # Remove the first character from the window and adjust the counts
            s_count[ord(s[i - 1]) - ord('a')] -= 1
            # Add the next character to the window and adjust the counts
            s_count[ord(s[i + len_p - 1]) - ord('a')] += 1

            # Check if the current window is an anagram
            if p_count == s_count:
                res.append(i)

        return res