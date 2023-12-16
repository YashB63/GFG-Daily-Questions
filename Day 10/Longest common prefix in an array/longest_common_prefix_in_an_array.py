class Solution:
    def longestCommonPrefix(self, arr, n):
        if not arr or n == 0:
            return "-1"
            
        min_length = min(len(s) for s in arr)
        result = ""
        
        for i in range(min_length):
            current_char = arr[0][i]
            
            for j in range(1,n):
                if arr[j][i] != current_char:
                    return result if result else "-1"
                    
            result += current_char 
            
        return result if result else "-1"