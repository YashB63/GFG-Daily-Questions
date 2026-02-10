class Solution:
    def computeLPSArray(self, str, M, lps):
        len = 0
        lps[0] = 0
        i = 1

        while (i < M):
            if (str[i] == str[len]):
                len += 1
                lps[i] = len
                i += 1
            else:  
                if (len != 0):
                    len = lps[len - 1]

                else:  
                    lps[i] = 0
                    i += 1

    def isRepeat(self, str):
        n = len(str)
        lps = [0] * n

        self.computeLPSArray(str, n, lps)

        length = lps[n - 1]

        return 1 if (length > 0 and n % (n - length) == 0) else 0