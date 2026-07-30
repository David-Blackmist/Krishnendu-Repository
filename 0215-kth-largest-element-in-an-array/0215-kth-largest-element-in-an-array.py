import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        result=[]
        for i in nums:
            heapq.heappush(result,i)
            if len(result)>k:
                heapq.heappop(result)
        return result[0]
        
        