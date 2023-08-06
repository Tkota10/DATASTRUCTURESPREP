
#This is the iterative solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

        stack = [(root, float('-inf'))]
        num_good = 0

        while stack:
            node, curmax = stack.pop()
            if curmax <= node.val:
                num_good += 1
            if node.left:
                stack.append((node.left, max(node.val, curmax)))
            if node.right:
                stack.append((node.right, max(node.val, curmax)))

        return num_good
    


#This is the recursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS, recursive, iterative search
        def search(root, curmax, num_good):
            if curmax <= root.val:
                num_good[0] += 1
            if root.left:
                search(root.left, max(root.val, curmax), num_good)
            if root.right:
                search(root.right, max(root.val, curmax), num_good)

        num_good = [0]  # Use a list to store the count as a mutable data structure
        search(root, float('-inf'), num_good)  # Start the search with negative infinity as the initial max value
        return num_good[0]