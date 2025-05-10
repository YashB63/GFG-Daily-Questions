class Solution:
    def findLongestWord (ob, S, d):
        n = len(d)
        ns = len(S)
        currentMax = ""
        for w in d:
            j = 0
            for i in range(ns):
                if w[j] == S[i]:
                    j += 1
                if j >= len(w):
                    if len(currentMax) == len(w):
                        currentMax = currentMax if currentMax < w else w
                    else:
                        currentMax = currentMax if len(currentMax) > len(w) else w 
                    break;
        
        return currentMax