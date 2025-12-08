class Solution:
    def extractMaximum(self,ss): 
        num, res, flag = 0, 0, 0

        for i in range(len(ss)): 
            if ss[i] >= "0" and ss[i] <= "9": 
                num = num * 10 + int(int(ss[i]) - 0) 
                flag = 1

            else: 
                res = max(res, num) 
                num = 0
    
        if flag == 1:
            return max(res, num) 
        else:
            return -1