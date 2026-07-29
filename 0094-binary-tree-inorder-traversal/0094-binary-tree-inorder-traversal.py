# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        def travel(node):
            if node==None:
                return
            travel(node.left)
            result.append(node.val)
            travel(node.right)
        travel(root)
        return result
        