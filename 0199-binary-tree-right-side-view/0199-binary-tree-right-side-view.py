class Solution(object):
    def rightSideView(self, root):
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
        ans=[]
        for i in range(len(result)):
            ans.append(result[i][-1])
        return ans
            
        