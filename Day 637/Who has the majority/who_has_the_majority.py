class Solution:
    def moreFrequent(self, arr, x, y):
        countX = arr.count(x)  
        countY = arr.count(y)  
        
        if countX > countY:
            return x
        elif countY > countX:
            return y
        else:
            return min(x, y)