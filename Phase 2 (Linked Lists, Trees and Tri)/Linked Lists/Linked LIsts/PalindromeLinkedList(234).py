class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        

        slow = fast = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # Handle odd number of elements
        if fast:
            slow = slow.next

        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next

        return True