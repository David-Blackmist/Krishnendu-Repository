# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        result=[]
        def travel(node,level):
            if node==None:
                return
            if len(result)==level:
                result.append([])
            result[level].append(node.val)
            travel(node.left,level+1)
            travel(node.right,level+1)
        travel(root,0)
        for i in range(len(result)):
            if i%2==1:
                result[i].reverse()
        return result
            
        