
# Correct Solution
        #Variables

        longlength = 0

        templength = 0
        unique_chars = set()

        start = 0
        end = 0


while end < len(s):
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            templength += 1
            longlength = max(longlength, templength)
            end += 1
        else:
            unique_chars.remove(s[start])
            start += 1
            templength -= 1

    return longlength


#My Original Solution (Passed a third of the testcases)

        while end < len (s):
            if s[end] in unique_chars:
                longlength = max (longlength, templength)
                start = end
                unique_chars.clear()
                unique_chars.add(s[start])
                templength = 1
            else:
                templength+=1
                unique_chars.add(s[end])
            end +=1
        return longlength