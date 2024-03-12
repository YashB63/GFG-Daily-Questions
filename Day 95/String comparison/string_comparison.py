class Solution:
    def stringComparsion(self, s1, s2):
        
        i = 0
        j = 0
        n = len(s1)
        m = len(s2)
        while i < n and j < m:
            if i+1 < n and j+1 < m and s1[i] == 'n' and s1[i+1] == 'g' and s2[j] == 'n' and s2[j+1] == 'g':
                i+=2
                j+=2
            elif i+1 < n and s1[i] == 'n' and s1[i+1] == 'g':
                if s2[j] > 'n':
                    return -1
                else:
                    return 1
            elif j+1 <m and s2[j] == 'n' and s2[j+1] == 'g':
                if s1[i] > 'n':
                    return 1
                else:
                    return -1
            elif s1[i] == s2[j]:
                i+=1
                j+=1
            elif s1[i] < s2[j]:
                return -1
            else:
                return 1
        if i == n and j == m:
            return 0
        if i < n:
            return 1
        else:
            return -1