class Solution:
    
    def recursiveSubsets(self, i, arr, s, ans):
        if i == len(arr):
            ans.append(s[:]) 
            return
        
        s.append(arr[i])
        self.recursiveSubsets(i+1, arr, s, ans)
        s.pop()
        self.recursiveSubsets(i+1, arr, s, ans)
        
    def subsets(self, arr):
        ans = []
        arr = list(set(arr))
        arr.sort() 
        self.recursiveSubsets(0, arr, [], ans)
        ans.sort()
        return ans