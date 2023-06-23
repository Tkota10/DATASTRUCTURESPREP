class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = self.maxHeight(root.left)
        right =  self.maxHeight(root.right)

        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        #Write a function that finds the left and reight
        #if the abs(left - right), return false
        #if you reach Null, then you return True

    
    def maxHeight(self, root):
        if root == None:
            return 0
        
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))