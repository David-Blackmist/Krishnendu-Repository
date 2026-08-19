class Solution(object):
    def pivotArray(self, nums, pivot):
        # low=0
        # mid=0
        # high=len(nums)-1
        # while mid <=high:
        #     if nums[mid]<pivot:
        #         nums[low],nums[mid]=nums[mid],nums[low]
        #         low +=1
        #         mid +=1
        #     elif nums[mid]==pivot:
        #         mid +=1
        #     elif nums[mid]>pivot:
        #         nums[mid],nums[high]=nums[high],nums[mid]
        #         high -=1
        low=[]
        mid=[]
        high=[]
        for i in nums:
            if i < pivot:
                low.append(i)
            elif i==pivot:
                mid.append(i)
            elif i>pivot:
                high.append(i)
        nums[:]=low+mid+high
        return nums
        