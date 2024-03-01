class Solution:
    def oddEven(ob, S):
        # code here 
        count = {}
        for i in range(len(S)):
            if S[i] in count:
                count[S[i]] += 1
            else:
                count[S[i]] = 1
        ans = 0
        for key in count:
            if count[key] %2 == 0 and ord(key)%2 == 0:
                ans += 1
            elif count[key]%2 == 1 and ord(key)%2 == 1:
                ans += 1
        if ans%2 == 0:
            return "EVEN"
        return "ODD"