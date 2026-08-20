class Solution(object):
    def frequencySort(self, nums):
        frq={}
        for i in nums:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i] +=1
        nums.sort(key=lambda x:(frq[x],-x))
        return nums