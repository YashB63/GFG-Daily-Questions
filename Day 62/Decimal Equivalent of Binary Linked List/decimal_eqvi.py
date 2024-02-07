class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        
        t, res, ans = head, 0, []
        while t:
            ans.append(t.data)
            t = t.next
        ans = ans[::-1]
        for i in range(len(ans)):
            res += (ans[i]*(2**i))%MOD
        return res%MOD