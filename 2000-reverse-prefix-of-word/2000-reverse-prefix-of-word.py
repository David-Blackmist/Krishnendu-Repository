class Solution(object):
    def reversePrefix(self, word, ch):
        idx=-1
        for i in range(len(word)):
            if word[i]==ch:
                idx=i
                break
        st=word[0:idx+1][::-1]
        return st+word[idx+1:]        