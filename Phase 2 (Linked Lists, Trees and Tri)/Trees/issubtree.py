def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        # if the roots are the same, then run a function that checks if the trees are the same
        if not subRoot:
            return True

        if not root:
            return False

        if self.check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check(self, root, subroot): #Compare if the two imports are the same
        if not root and not subroot:
            return True

        if root and subroot and root.val == subroot.val:
            return self.check(root.left, subroot.left) and self.check(root.right, subroot.right)
        
        return False