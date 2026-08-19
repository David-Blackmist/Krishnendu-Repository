class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result=[]
        new_interval=intervals[0]
        result.append(new_interval)
        for i in intervals:
            if i[0]<=new_interval[1]:
                new_interval[1]=max(i[1],new_interval[1])
            else:
                new_interval=i
                result.append(i)
        return result
        