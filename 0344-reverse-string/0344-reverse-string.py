class Solution(object):
    def reverseString(self, s):
        k=0
        j=len(s)-1
        while k<j :
            s[k],s[j]=s[j],s[k]
            k +=1
            j -=1
        return s

        