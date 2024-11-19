class Solution:
    def convHex(self, num):
        temp = ''
        rem = 0
        
        while num!=0:
            rem = num % 16
            c = 0
            
            if rem<10:
                c = rem + 48
            else:
                c = rem + 87
                
            temp += chr(c)
            num = num // 16
            
        return temp
        
    def encryptString(self, S):
        N = len(S)
        i=0
        ans = ""
        
        while i<N:
            ch = S[i]
            count = 0
            
            while (i<N) and (S[i]==ch):
                count += 1
                i += 1
                
            hexw = self.convHex(count)
            ans += ch
            ans += hexw
            
        ans = ans[::-1]
        return ans