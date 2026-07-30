class Solution(object):
    def searchBST(self, root, val):
        if root==None:
            return None
        curr=root
        while curr!=None:
            if curr.val==val:
                return curr
            elif curr.val<val:
                curr=curr.right
            elif curr.val>val:
                curr=curr.left
        return None