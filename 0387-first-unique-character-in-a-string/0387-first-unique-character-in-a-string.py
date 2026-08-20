class Solution(object):
    def firstUniqChar(self, s):
        frq={}
        for i in s:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i]+=1
        for j in range(len(s)):
            if frq[s[j]]==1:
                return j
        return -1
        