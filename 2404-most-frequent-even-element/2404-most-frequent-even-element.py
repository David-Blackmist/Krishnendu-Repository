class Solution(object):
    def mostFrequentEven(self, nums):
        frq={}
        for i in nums:
            if i %2==0:
                if i not in frq:
                    frq[i]=1
                elif i in frq:
                    frq[i] +=1
        if not frq:
            return -1
        ans=-1
        max_count=0
        for key,value in frq.items():
            if value>max_count or (value==max_count and key<ans):
                ans=key
                max_count=value
        return ans


        