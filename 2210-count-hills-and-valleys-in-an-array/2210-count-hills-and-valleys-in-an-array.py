class Solution(object):
    def countHillValley(self, nums):
        arr1=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!= nums[i-1]:
                arr1.append(nums[i])
        count=0
        for j in range(1,len(arr1)-1):
            if (arr1[j] > arr1[j-1] and arr1[j] > arr1[j+1]):
                count +=1
            elif (arr1[j]<arr1[j-1] and arr1[j]<arr1[j+1]):
                count +=1
        return count

                
        