class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        #we use fast, incase there's a NULL
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
