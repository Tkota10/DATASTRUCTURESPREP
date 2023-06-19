class Solution(object):
    def removeNthFromEnd(self, head, n):

        #find a way to get a pointer to thhe end of the Linked List
        # Count down to the desired value
        #remove value when needed


        #1) Possible way is to reverse a linked list. 2) Then count until n value. 3) Remove the value 4) Then remove it again
        
        # Create two pointers, fast and slow, and initialize them to the head of the linked list
        slow = head
        fast = head

        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # If the fast pointer reaches the end, it means we need to remove the head of the linked list
        if fast is None:
            return head.next

        # Move both pointers until the fast pointer reaches the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end by updating the next pointer of the previous node
        slow.next = slow.next.next

        return head