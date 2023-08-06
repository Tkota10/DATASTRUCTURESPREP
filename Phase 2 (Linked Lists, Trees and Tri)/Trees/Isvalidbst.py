#Recursive solution

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

        def dfs(root , min_val, max_val): #We have to keep track of the global min and max val
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False
            
            left = dfs(root.left, min_val, root.val)
            right = dfs(root.right, root.val, max_val)
            
            return left and right
            

        return dfs(root, float('-inf'), float('inf'))
        