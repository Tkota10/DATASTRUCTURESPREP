# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #l1 and l2 are pointers to the head of the list

        #add an entire list

        #Loop through each list and add up until you have a toal number 

        #Then add the elements 

        #Make a new Linked List
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2:
            cursum = carry #Starting with any digits still left over from the past

            if l1: #If there's digits left
                cursum += l1.val
                l1 = l1.next

            if l2: #If there's digits left
                cursum += l2.val
                l2 = l2.next


            carry = cursum // 10
            current.next = ListNode(cursum % 10) # First element is added to the next element
            current = current.next
        
        if carry > 0:
            current.next = ListNode(carry)
            
        #Now we have the result array

        return dummy_head.next  
        