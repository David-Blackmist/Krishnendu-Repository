class Solution(object):
    def removeDuplicates(self, s, k):
        result=[]
        for i in s:
            if len(result)!=0 and result[-1][0]==i:
                result[-1][1] +=1
                if result[-1][1]==k:
                    result.pop()
            else:
                result.append([i,1])
        string=""
        for char,count in result:
            string +=char*count
        return string
        