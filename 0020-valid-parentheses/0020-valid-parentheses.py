class Solution(object):
    def isValid(self, s):
        if len(s)%2==1:
            return False
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if i==")" and top!="(":
                    return False
                elif i=="}" and top!="{":
                    return False
                elif i=="]" and top !="[":
                    return False
        return len(stack)==0      