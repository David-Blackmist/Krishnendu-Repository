class Solution(object):
    def isPerfectSquare(self, num):
        i=0
        while i*i<=num:
            if i*i==num:
                return True
            i=i+1
        return False
        