class Solution:
    def pattern (self, arr):
        
        rows = []
        m = len(arr)
        for i in range(0, m):
            rows.append("".join([str(val) for val in arr[i]]))
        
        for i in range(0, m):
            if rows[i] == rows[i][::-1]:
                return "{} R".format(i)
        for i in range(0, m):
            j, k = 0, m-1
            while j<k:
                if rows[j][i] != rows[k][i]:
                    break
                j+=1
                k-=1
            if j>=k:
                return "{} C".format(i)
        return "-1"