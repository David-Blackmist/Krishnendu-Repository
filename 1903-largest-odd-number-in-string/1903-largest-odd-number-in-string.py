class Solution(object):
    def largestOddNumber(self, num):
        num_list=[]
        for i in num:
            num_list.append(int(i))   
        number=[]
        for j in range(len(num_list)-1,-1,-1):
            if num_list[j]%2!=0:
                number=num_list[:j+1]
                break
        return "".join(map(str,number))
                    