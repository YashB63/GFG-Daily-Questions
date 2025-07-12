class Solution:
    def find (self, N):
        x = 0
        for x in range(N, 0, -1): 
            no = x 
            prev_dig = 11
      
            flag = True
            while (no != 0): 
                if (prev_dig < no % 10): 
                    flag = False
                    break
                  
                prev_dig = no % 10
                no //= 10
      
            if (flag == True): 
                break
        return x 