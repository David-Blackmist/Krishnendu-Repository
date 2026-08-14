from collections import Counter
class Solution(object):
    def maximumLengthSubstring(self, s):
        longest=0
        window_occ=Counter()
        start=0
        for end in range(len(s)):
            leading_element=s[end]
            window_occ[leading_element]+=1
            while window_occ[leading_element]>2:
                window_occ[s[start]] -=1
                start +=1
            longest=max(end-start+1,longest)
        return longest
        
            