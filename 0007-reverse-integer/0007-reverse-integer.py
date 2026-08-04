class Solution:
    def reverse(self,n):
        if n==0:
            return 0
        absolute=abs(n)
        reverse=int(str(absolute)[::-1])
        if n<0:
            reverse=-reverse
        if reverse < -(2**31) or reverse > (2**31 -1):
            return 0
        return reverse
            


        
        