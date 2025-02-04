class Solution:
    def findPermutation(self, s):
        if len(s) == 0:
            return [""]
    
        result = set()  
    
        for i in range(len(s)):

            current_char = s[i]

            remaining_string = s[:i] + s[i+1:]
    
            remaining_permutations = self.findPermutation(remaining_string)
    
            for perm in remaining_permutations:
                result.add(current_char + perm)
    
        return list(result)