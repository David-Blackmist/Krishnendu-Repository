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
        
