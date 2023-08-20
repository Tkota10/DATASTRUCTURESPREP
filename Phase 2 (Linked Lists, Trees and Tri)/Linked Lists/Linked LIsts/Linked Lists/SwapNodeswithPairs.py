# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        '''
        Flip every other:

        Two Pointers:
        #Fast and slow pointer,

        #Swap at eachh point

        '''

        dummy = ListNode(0, head)

        prev, curr = dummy, head #I want to set all the values to be equal to dummy

        while curr and curr.next: # we have atleast two nodes

            #Save ptrs we can use
            nxtPair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nxtPair
            prev.next = second #Put in the first position

            prev = curr
            curr = nxtPair
        
        return dummy.next
    

'''
Essentially move in pairs

Have elements one from each other

Then swamp the element, and then move across two

Make a dummy node so every element has a predecessor
'''