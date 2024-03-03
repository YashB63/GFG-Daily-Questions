class Solution:
    def generate_binary_string(self,s):
        
        res = [s]
        
        for i, c in enumerate(s):
            if c == '?':
                for j in range(len(res)):
                    tmp = list(res.pop(0))
                    tmp[i] = '0'
                    res.append(''.join(tmp))
                    tmp[i] = '1'
                    res.append(''.join(tmp))
        return res