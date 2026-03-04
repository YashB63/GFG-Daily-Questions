class Solution:
    def isPanagram(self,s):
        arr = [0] * 26
        s = s.lower()
        for char in s:
            arr[ord(char) - ord('a')] += 1

        for i in arr:
            if i == 0:
                return False
            
        return True