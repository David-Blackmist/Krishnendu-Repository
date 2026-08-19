class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        if len(words)==0:
            return ""
        vowel=set("aeiouAEIOU")
        def get_count(words):
            count=0
            for i in words:
                if i in vowel:
                    count +=1
            return count
        target=get_count(words[0])            
        result=[words[0]]
        for j in words[1:]:
            if get_count(j)==target:
                result.append(j[::-1])
            else:
                result.append(j)
        return " ".join(result)


        
        