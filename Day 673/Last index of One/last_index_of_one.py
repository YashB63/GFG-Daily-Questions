class Solution:
    def lastIndex(self, s: str) -> int:
        flag = False  
        n = len(s)  
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                flag = True  
                return i  

        if not flag:
            return -1