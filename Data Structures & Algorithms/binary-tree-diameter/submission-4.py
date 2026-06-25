# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
    
        def height(node):
            
            if node == None: #if not node
                return 0

            leftHeight = height(node.left) #0 #0 #1 #2 #3 #4
            rightHeight = height(node.right) #0
            
            self.diameter = max(self.diameter, leftHeight + rightHeight)
            return 1 + max(leftHeight,rightHeight)

        height(root)
        return self.diameter
