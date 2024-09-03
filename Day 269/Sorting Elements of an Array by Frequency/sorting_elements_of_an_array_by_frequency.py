class Solution:
    def sortByFreq(self,arr):
        mp = {}
        for i in range(len(arr)):
            if arr[i] in mp:
                mp[arr[i]] +=1
            else:
                mp[arr[i]] = 1
        
        a = []
        for k,v in mp.items():
            a.append([k,v])
        a.sort()
        a.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for k,v in a:
            
            for i in range(v):
                ans.append(k)
        return ans