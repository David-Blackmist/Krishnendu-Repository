class Solution(object):
    def largestPerimeter(self, nums):
        arr=(sorted(nums,reverse=True))
        for i in range(len(arr)-2):
            if arr[i]<arr[i+1]+arr[i+2]:
                return arr[i]+arr[i+1]+arr[i+2]
        return 0

        