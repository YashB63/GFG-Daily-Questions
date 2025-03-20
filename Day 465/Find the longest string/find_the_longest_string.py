class Solution():
    def longestString(self, arr, n):
        arr.sort()
        words = set(arr)
        longest = ""
        
        for word in arr:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in words:
                    valid = False
                    break
            
            if valid:
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        
        return longest