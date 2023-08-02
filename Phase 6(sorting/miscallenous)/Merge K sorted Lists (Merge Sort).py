#Merge sort solution:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists #Keep on adding them together
        return lists[0]



    def mergeLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy


        #Create a dummy Node so you don't have to worry about inputting into an empty list
        #Like if we tried inputting into list1 and list2
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1 #extra stuff left over
        else:
            tail.next = list2 #extrastuff left over

        return dummy.next
    



    #heap Solution

    class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        heap = []
        cur = ListNode()
        dummy = cur

        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        
        return dummy.next