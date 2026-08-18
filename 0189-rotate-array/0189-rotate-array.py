class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        if k==0:
            return nums
        nums[:]=nums[-k:]+nums[:-k]
        return nums
        