class Solution(object):
    def frequencySort(self, s):
        frq={}
        for i in s:
            if i not in frq:
                frq[i]=1
            elif i in frq:
                frq[i] +=1
        sorted_char=sorted(frq.keys(),key=lambda x:(frq[x]),reverse=True)
        result=[]
        for j in sorted_char:
            j=j*frq[j]
            result.append(j)
        return "".join(result)
        