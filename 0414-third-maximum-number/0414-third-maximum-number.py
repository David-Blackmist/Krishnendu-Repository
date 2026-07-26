class Solution(object):
    def thirdMax(self, nums):
        arr=[]
        for i in nums:
            if i not in arr:
                arr.append(i)
        arr.sort()
        if len(arr)<3:
            return max(arr)
        else:
            return arr[-3]

        