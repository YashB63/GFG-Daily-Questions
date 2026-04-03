class Solution:
    def posNegPair(self, arr):
        freq={}
        
        for num in arr:
            if(num in freq):
                freq[num]+=1
            else:
                freq[num]=1
        
        negatives=sorted([num for num in freq if(num<0)],key=abs)
        ans=[]
        
        for num in negatives:
            if(-num in freq):
                min_value=min(freq[num],freq[-num])
                
                for _ in range(min_value):
                    ans.append(num)
                    ans.append(-num)
        
        return ans