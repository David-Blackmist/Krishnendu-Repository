class Solution(object):
    def firstMissingPositive(self, nums):
        s1=set(nums)
        target=1
        while target in s1:
            target +=1
        return target
        