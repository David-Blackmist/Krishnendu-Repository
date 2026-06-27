class Solution(object):
    def checkIfPangram(self, sentence):
        frq_map={}
        for i in sentence:
            if i not in frq_map:
                frq_map[i]=1
            elif i in frq_map:
                frq_map[i] +=1
        map_length=len(frq_map)
        if map_length==26:
            return True
        else:
            return False
                