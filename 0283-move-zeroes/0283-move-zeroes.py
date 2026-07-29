class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==0:
            return nums
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[l],nums[i]=nums[i],nums[l]
                l=l+1
        return nums
        


        