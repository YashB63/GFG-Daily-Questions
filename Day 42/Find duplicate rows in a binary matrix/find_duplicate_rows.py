class Solution:
    def repeatedRows(self, arr, m ,n):
        
        x = []
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if(arr[i] == arr[j]):
                    if(j not in x):
                        x.append(j)
        return sorted(x)