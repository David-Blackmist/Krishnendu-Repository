class Solution(object):
    def plusOne(self, digits):
        result=int("".join(map(str,digits)))+1
        new=[]
        for i in str(result):
            new.append(int(i))
        return new
        