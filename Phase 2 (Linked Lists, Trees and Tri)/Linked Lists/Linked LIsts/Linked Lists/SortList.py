# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next

    def sortList(self, head):

        #Find the middle:


        if not head or not head.next:
            return head
        

        slow = head
        fast = head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(mid)

        return self.merge(l1, l2)
        """
        :type head: ListNode
        :rtype: ListNode
        """