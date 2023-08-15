class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:


        '''
            Store all of nodes in B in a Hashmap (To get O(1) lookup)


        '''

        Node_Map = {}


        #Put all the nodes of LinkedList B into a hashmap
        while headB:
            Node_Map[headB] = headB.val
            headB = headB.next
        

        while headA:
            if headA in Node_Map:
                return headA
            headA = headA.next

        return None