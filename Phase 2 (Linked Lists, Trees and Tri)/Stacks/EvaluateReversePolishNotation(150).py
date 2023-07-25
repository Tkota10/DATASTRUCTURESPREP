class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        hashSet = {"*", "-", "+", "/"}
        for token in tokens:
            if token in hashSet:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand2 - operand1)
                elif token == "*":
                    stack.append(operand2 * operand1)
                else:
                    stack.append(int(float(operand2) / operand1) if operand2 * operand1 >= 0 else -int(abs(operand2) / abs(operand1)))

            else:
                stack.append(int(token))

        return stack.pop()
    
    #Takeaways (We don't hahe to make a complicated dictionary)