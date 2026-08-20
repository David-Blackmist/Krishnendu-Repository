class Solution(object):
    def divideArray(self, nums):
        if len(nums)%2!=0:
            return False
        frq={}
        for i in nums:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i]+=1
        for j in frq.values():
            if j%2!=0:
                return False
        return True
        