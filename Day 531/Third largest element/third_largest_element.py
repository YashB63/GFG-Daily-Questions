class Solution:
    def thirdLargest(self, arr):
        n = len(arr)
        big1 = -1  
        big2 = -1  
        big3 = -1  

        for i in arr:
            if i > big3:  
                big3 = i  

            if big3 > big2:  
                big2, big3 = big3, big2  

            if big2 > big1: 
                big1, big2 = big2, big1 
                
        return big3