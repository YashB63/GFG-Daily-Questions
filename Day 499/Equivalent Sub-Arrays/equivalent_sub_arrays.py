class Solution:
    def countDistinctSubarray(self,arr, n): 
        dis = len(set(arr))  
        left = 0
        res = 0
        hashmap = {}
    
        for right in range(n):
            hashmap[arr[right]] = hashmap.get(arr[right], 0) + 1
    
            while len(hashmap) == dis:
                res += (n - right)  
                hashmap[arr[left]] -= 1
                if hashmap[arr[left]] == 0:
                    del hashmap[arr[left]]
                left += 1
    
        return res