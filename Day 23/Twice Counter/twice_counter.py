class Solution:
    def countWords(self,List, n):
        
        x = {}
        
        for i in List:
            if i not in x:
                x[i] = 1
            else:
                x[i] += 1
                
        count = 0 
        
        for i in x.values():
            if  i == 2:
                count += 1
                
        return count