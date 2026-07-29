class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)
        return max(leftheight,rightheight)+1
        
        