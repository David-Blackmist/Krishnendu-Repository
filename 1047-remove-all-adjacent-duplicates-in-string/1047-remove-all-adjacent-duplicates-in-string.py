class Solution(object):
    def removeDuplicates(self, s):
        result=[]
        for i in s:
            if len(result)!=0 and result[-1]==i :
                result.pop()
            else:
                result.append(i)
        return "".join(result)
        