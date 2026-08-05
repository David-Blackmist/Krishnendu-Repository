class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        left=0
        right=len(nums)-1
        answer=0
        while left<right:
            pair_sum=nums[left]+nums[right]
            maximum=max(answer,pair_sum)
            answer=maximum
            left=left+1
            right=right-1
        return answer
        
        