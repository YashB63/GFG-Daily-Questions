class Solution:
    def stringMirror(self, str : str) -> str:
        
        prev = ""
        for i in range(len(str)):
            if prev == "" or prev > str[:i+1]:
                prev = str[:i+1] + str[:i+1][::-1]
                
        return prev