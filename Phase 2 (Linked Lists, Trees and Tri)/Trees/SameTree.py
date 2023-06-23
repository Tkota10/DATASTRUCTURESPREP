# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        #Two Nulls, that would require they be the same, since two nulls would be the same

        if not p and not q:
            return True
        
        #One Null, one not would be wrong since they would be different

        if not q or not p:
            return False

        #if the elements are the same, you move on with children. If their different, that means they aren't the same tree
        
        if p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) 
            
        else:
            return False