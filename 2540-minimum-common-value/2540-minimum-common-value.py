class Solution(object):
    def getCommon(self, nums1, nums2):
        arr=list(set(nums1) & set(nums2))
        arr.sort()
        for i in arr:
            if i in nums1 and nums2:
                return i
        return -1               