class Solution(object):
    def deleteDuplicates(self, head):
        prev, curr = None, head

        #Make a set and add values into it
        unique_values = set()
        while curr:
            if curr.val in unique_values:
                #This will delete the linked list node
                prev.next = curr.next
                curr = curr.next
            else:
                #It is not in the set
                unique_values.add(curr.val)
                prev = curr
                curr = curr.next
        return head