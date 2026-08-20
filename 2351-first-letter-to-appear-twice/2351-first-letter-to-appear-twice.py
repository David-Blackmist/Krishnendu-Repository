class Solution(object):
    def repeatedCharacter(self, s):
        seen=set()
        for i in s:
            if i not in seen:
                seen.add(i)
            elif i in seen:
                return i
        
        