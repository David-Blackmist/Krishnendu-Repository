class Solution(object):
    def averageOfLevels(self, root):
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
            ans.append(float(sum(result[i])) / len(result[i]))
        return ans

        
        