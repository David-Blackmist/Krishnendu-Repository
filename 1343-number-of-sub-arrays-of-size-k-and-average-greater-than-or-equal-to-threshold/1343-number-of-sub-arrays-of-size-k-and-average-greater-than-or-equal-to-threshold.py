class Solution(object):
    def numOfSubarrays(self, nums, k, threshold):
        curr_sum=sum(nums[:k])
        count=0
        avg=float(curr_sum)/k
        if avg>=threshold:
            count=count+1
        for i in range(len(nums)-k):
            curr_sum=curr_sum - nums[i]
            curr_sum=curr_sum+ nums[i+k]
            avg=float(curr_sum)/k
            if avg>=threshold:
                count  +=1
        return count       
                    