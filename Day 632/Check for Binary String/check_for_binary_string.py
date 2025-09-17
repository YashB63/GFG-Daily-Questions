class Solution:
    def isBinary(self, str):
        cnt = 0
        
        for i in str:
            if (i == '0' or i == '1'):
                cnt += 1

        if (cnt == len(str)):
            return (True)

        return (False)