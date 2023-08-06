class Solution(object):
    def levelOrder(self, root):
     """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        #Maximum height of the graph

        res = []

        if not root:
            return res

        def helper(root, level):

            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)

            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)
        
        helper(root, 0)

        return res