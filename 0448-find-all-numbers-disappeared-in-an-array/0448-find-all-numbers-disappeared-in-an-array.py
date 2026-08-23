class Solution(object):
    def findDisappearedNumbers(self, nums):
        s1=set(nums)
        arr1=[]
        for i in range(1,len(nums)+1):
            if i not in s1:
                arr1.append(i)
        return arr1
            
        