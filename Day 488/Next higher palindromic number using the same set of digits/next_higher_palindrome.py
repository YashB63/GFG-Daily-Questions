class Solution:
    def nextPalin(self,s):
        n = len(s)
        if n < 4:
            return -1
        end = n//2 - 1
        rptr = end
        while rptr > 0:
            if s[rptr] > s[rptr-1]:
                break
            rptr -= 1
        if rptr == 0:
            return -1
        lptr = rptr - 1
        rptr += 1
        while rptr <= end and s[rptr] > s[lptr]:
            rptr += 1
        rptr -= 1
        s = list(s)
        s[lptr], s[rptr] = s[rptr], s[lptr]
        new = s[:lptr+1] + s[lptr+1:end+1][::-1]
        if n%2==0:
            new.extend(new[::-1])
        else:
            new += [s[n//2]] + new[::-1]
        return ''.join(new)