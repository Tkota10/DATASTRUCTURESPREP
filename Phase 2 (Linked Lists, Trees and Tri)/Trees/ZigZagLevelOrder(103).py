from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [] 
        queue = deque([(root, 0)])
        
        while queue:
            level_vals = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node, i = queue.popleft()
                level_vals.append(node.val)
                
                if node.left:
                    queue.append((node.left, i + 1))
                if node.right:
                    queue.append((node.right, i + 1))
            
            if len(res) % 2 == 1:
                res.append(level_vals[::-1])  # Append the level values in reverse order
            else:
                res.append(level_vals)
        
        return res