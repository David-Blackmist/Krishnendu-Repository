class Solution(object):
    def singleNumber(self, nums):
        frq={}
        for i in nums:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i]+=1
        for key,value in frq.items():
            if value ==1:
                return key
        