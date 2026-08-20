class Solution(object):
    def majorityElement(self, nums):
        frq={}
        for i in nums:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i] +=1
        target=(len(nums))//3
        result=[]
        for key,value in frq.items():
            if value>target:
                result.append(key)
        return result
        