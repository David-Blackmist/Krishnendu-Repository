class Solution(object):
    def findDifference(self, nums1, nums2):
        arr1=[]
        for i in nums1:
            if i not in nums2 and  i not in arr1:
                arr1.append(i)
        arr2=[]
        for j in nums2 :
            if j not in nums1 and j not in arr2:
                arr2.append(j)
        return [arr1,arr2]
        