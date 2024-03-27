class Solution:
    def fourSum(self, arr, k):
        
        s = set()
        ans = []
        n = len(arr)
        
        arr.sort()
        
        a, b, c, d = 0, 1, 2, n-1
        while a < n-3:
            if a>0 and arr[a]==arr[a-1]:
                a+=1
                continue
            b = a+1
            while b < n-2:
                if b>a+1 and arr[b]==arr[b-1]:
                    b+=1
                    continue
                c, d = b+1, n-1
                while c < d:
                    x = arr[a]+arr[b]+arr[c]+arr[d]
                    if x == k:
                        t = [arr[a], arr[b], arr[c], arr[d]]
                        t.sort()
                        w = ''.join(map(str, t))
                        if w not in s:
                            ans.append(t)
                            s.add(w)
                        d -= 1
                    elif x > k:
                        d -= 1
                    else:
                        c += 1
                    
                b += 1
            a += 1
        
        return ans  