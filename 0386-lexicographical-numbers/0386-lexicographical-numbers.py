class Solution(object):
    def lexicalOrder(self, n):
        arr=[]
        for i in range(1,n+1):
            arr.append(str(i))
        arr.sort()
        for i in range(len(arr)):
            arr[i]=int(arr[i])
        return arr

        