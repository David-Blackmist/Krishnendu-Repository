from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start=0
        longest=0
        window_counter=Counter()
        for end in range(len(s)):
            window_counter [s[end]]+=1
            while window_counter [s[end]]>1:
                window_counter[s[start]]-=1
                start +=1
            longest=max(end-start+1,longest)
        return longest
        