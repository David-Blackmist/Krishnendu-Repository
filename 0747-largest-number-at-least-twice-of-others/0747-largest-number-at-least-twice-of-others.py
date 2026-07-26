class Solution(object):
    def dominantIndex(self, nums):
        if len(nums)==1:
            return 0
        max1=max(nums)
        idx=nums.index(max1)
        arr=sorted(nums)
        if max1>=arr[-2]*2:
            return idx
        else:
            return -1
        
        