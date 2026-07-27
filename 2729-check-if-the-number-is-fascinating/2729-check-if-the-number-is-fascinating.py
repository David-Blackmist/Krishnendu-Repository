class Solution(object):
    def isFascinating(self, n):
        double=2*n
        triple=3*n
        join=str(n)+str(double)+str(triple)
        mp={}
        for i in join:
            if i=="0":
                return False
            if i in mp:
                mp[i] +=1
            elif i not in mp:
                mp[i]=1
        for j in mp.values():
            if j!=1:
                return False
        return len(mp)==9
        
        