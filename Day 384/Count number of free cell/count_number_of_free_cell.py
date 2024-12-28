class Solution():
    def countZero(self, n, k ,arr):
        r=set()
        c=set()
        b=n*n
        l=[]
        for i in range(k):
            a=0
            if arr[i][0] not  in r:
                a=a+n-len(c)
                r.add(arr[i][0])
            if(arr[i][1]) not in c:
                a=a+n-len(r)
                c.add(arr[i][1])
            b=b-a
            if(b<0):
                l.append(0)
            else:
                l.append(b)
        return l