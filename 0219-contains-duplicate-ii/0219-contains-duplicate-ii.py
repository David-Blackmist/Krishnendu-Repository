class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen={}
        for idx,num in enumerate(nums):
            if num in seen:
                if idx-seen[num]<=k:
                    return True
            seen[num]=idx
        return False
            
        