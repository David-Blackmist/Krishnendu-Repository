class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        curr_ar=0
        max_ar=0
        while left<right:
            distance=right-left
            curr_ar=(min(height[left],height[right])*distance)
            if curr_ar>max_ar:
                max_ar=curr_ar
            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        return max_ar
