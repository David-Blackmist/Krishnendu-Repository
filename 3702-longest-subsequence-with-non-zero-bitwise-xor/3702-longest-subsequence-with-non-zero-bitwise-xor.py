class Solution(object):
    def longestSubsequence(self, nums):
        result=0
        for i in nums:
            result ^=i
        if result !=0:
            return len(nums)
        for j in range(len(nums)):
            if nums[j] != 0:
                return len(nums)-1
        return 0
        