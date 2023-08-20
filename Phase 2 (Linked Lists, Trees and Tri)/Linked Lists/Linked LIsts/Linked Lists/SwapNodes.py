# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:



        '''
        Go through until I reach the kth element:

        Then go to the end, while restarting a pointer at the beginning

        When I reach the end, then I'll have the right element

        Swap the elements

        '''

        if not head:
            return head

        curr = head

        for i in range(k-1):
            curr = curr.next
        
        left = curr #Now this contains the leftmost element

        right = head

        while curr and curr.next:
            curr = curr.next
            right = right.next

        
        #Swap the left and right values

        left.val, right.val = right.val, left.val

        return head
