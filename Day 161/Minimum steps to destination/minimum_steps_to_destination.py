class Solution:
    def minSteps(self, d):
        
        temp = 0
        step = 0
        
        while(temp < d):
            temp += step
            step += 1
        while((temp - d) % 2 == 1):
            temp += step
            step += 1
        
        return step - 1