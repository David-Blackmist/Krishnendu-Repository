class Solution(object):
    def backspaceCompare(self, s, t):
        st_s=[]
        st_t=[]
        for i in s:
            if i =="#":
                if len(st_s)>0:
                    st_s.pop()
            else:
                st_s.append(i)
        for j in t:
            if j =="#":
                if len(st_t)>0:
                    st_t.pop()
            else:
                st_t.append(j)
        if "".join(st_s)=="".join(st_t):
            return True
        else:
            return False
        
        