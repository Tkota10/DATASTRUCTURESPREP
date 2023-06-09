    def detectCycle(self, head):
        fast = head
        num_val = set()
        #we use fast, incase there's a NULL
        while fast:
            if fast in num_val:
                return fast
            num_val.add(fast) #Very Helpful function. Make sure to use the add function in Hashmap
            fast = fast.next
        return