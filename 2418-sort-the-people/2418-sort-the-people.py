class Solution(object):
    def sortPeople(self, names, heights):
        arr=list(zip(names,heights))
        sorted_arr=sorted(arr,key=lambda x:x[1],reverse=True)
        result=[]
        for i in sorted_arr:
            result.append(i[0])
        return result
        