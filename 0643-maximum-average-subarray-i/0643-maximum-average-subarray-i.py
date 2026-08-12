class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=sum(nums[:k])
        max_sum=curr_sum
        for i in range(len(nums)-k):
            curr_sum=curr_sum-nums[i]
            curr_sum=curr_sum+nums[i+k]
            max_sum=max(max_sum,curr_sum)
        return float(max_sum)/k      