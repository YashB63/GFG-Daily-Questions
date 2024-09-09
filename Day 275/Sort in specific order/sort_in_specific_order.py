class Solution:
    
    def sortIt(self, arr):
        o_arr=[i for i in arr if i%2!=0]
        o_arr.sort(reverse=True)
        e_arr=[i for i in arr if i%2==0]
        e_arr.sort()
        arr[:]=o_arr+e_arr
        return arr