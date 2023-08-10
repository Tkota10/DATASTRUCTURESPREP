# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        #DFS Search

        #At every element, add the element

        res = []
        def dfs(root, targetsum, path):
            if not root: 
                return

            targetsum -= root.val
            path.append(root.val)
            
            if not root.left and not root.right and targetsum == 0: #If it's a leaf node and the targetsum is zero
                res.append(path[:])
            
            dfs(root.left , targetsum , path)
            dfs(root.right , targetsum , path)

            path.pop()

            

    
        dfs(root, targetSum , [])

        return res