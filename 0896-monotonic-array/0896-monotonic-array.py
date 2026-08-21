class Solution(object):
    def isMonotonic(self, nums):
        arr1=sorted(nums)
        arr2=sorted(nums,reverse=True)
        if nums==arr1 or nums==arr2:
            return True
        return False
        