class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i in range(n):
            curr_temp=temperatures[i]
            while stack and curr_temp>temperatures[stack[-1]]:
                prev_day=stack.pop()
                ans[prev_day]=i-prev_day
            stack.append(i)
        return ans
        