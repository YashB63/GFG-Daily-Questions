class Solution:
    def ExtractNumber(self,sentence):
        
        max = -1
        l = sentence.split(" ")
        for i in l:
            if i.isdigit() and "9" not in i and int(i)>max:
                max = int(i)
        
        return max