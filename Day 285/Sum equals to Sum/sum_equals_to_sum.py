class Solution:
    def findPairs(self, arr): 
        frq={}
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                sm=arr[i]+arr[j]
                if sm not in frq:
                    frq[sm]=1
                else:
                    return True
        return False