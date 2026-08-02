class Solution(object):
    def isPalindrome(self, s):
        text=""
        for i  in s:
            if i.isalnum():
                text +=i
        lower=text.lower()
        if lower==lower[::-1]:
            return True
        else:
            return False

        