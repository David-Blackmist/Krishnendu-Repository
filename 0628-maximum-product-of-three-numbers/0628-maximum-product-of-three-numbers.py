class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        prdct1=nums[-1]*nums[-2]*nums[-3]
        prdct2=nums[0]*nums[1]*nums[-1]
        if prdct1>=prdct2:
            return prdct1
        else:
            return prdct2
        