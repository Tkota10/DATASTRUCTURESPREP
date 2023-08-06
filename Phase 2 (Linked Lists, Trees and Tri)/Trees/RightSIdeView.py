class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        #Dfs: Looking at the right side of it (Thinking about how you want to order righht and left)
        res = []
        def search(root,level):
            if root:
                if len(res) == level:
                    res.append(root.val)
                search(root.right, level + 1)
                search(root.left, level + 1)
        
        search(root, 0)

        return res