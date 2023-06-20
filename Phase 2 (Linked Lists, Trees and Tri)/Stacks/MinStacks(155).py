class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #First add the elemeent (if the thing is empty)

        if not self.stack:
            self.stack.append((val,val))
            #append only takes one argument which is why we have to do the double parenthesis
            return
        
        #Find the min
        current_min = self.stack[-1][-1]
        if val < current_min:
            self.stack.append((val, val))
        else:
            self.stack.append((val, current_min))
        return
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        #Don't know how this works
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
   