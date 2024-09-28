class Solution:
    def countNumbers(self, n):
        count = 0 
        for i in range(1, n+1):
            while i:
                lastdigit = i%10 
                if lastdigit<1 or lastdigit>5:
                    break 
                i //= 10 
                
            else:
                count+=1 
                    
        return count