class Solution:

    def permutation(self, s):
        res = []
        op, ip = s[0], s[1:]
        def recur(op, ip):
            if len(ip) == 0:
                res.append(op[:])
                return
            recur(op+" "+ip[0], ip[1:])
            recur(op+ip[0], ip[1:])
            
        recur(op, ip)
        return sorted(res)