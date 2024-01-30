class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    
    def fractionalknapsack(self, W,arr,n):
        
        cap = 0
        res = 0
        
        arr.sort(key = lambda x:x.value / x.weight, reverse=True)
        
        for item in arr:
            if cap + item.weight <= W:
                cap += item.weight
                res += item.value
                
            elif cap == W:
                break
            
            else:
                
                rem = W - cap
                res += rem * (item.value / item.weight)
                cap += rem
                
        return res