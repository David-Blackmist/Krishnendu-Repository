class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==0:
            return nums
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
        return nums
        


        