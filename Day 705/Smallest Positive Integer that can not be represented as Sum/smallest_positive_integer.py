class Solution:
    def smallestpositive(self, array, n): 
        array.sort()
        
        result = 1
        
        for i in range(n):
            if(array[i] <= result):
                result = result + array[i]
        
        return result