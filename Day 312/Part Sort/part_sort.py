class Solution:
	def partSort(self, arr, n, l, r):
        li_1 =[]
        li_2 =[]
        li_3 =[]
        if l > r:
            l,r =r,l
        for i in range(0,l):
            li_1.append(arr[i])
        for i in range(l,r+1):
            li_2.append(arr[i])
        li_2.sort()
        li_3 = li_1 + li_2
        for i in range(0, len(li_3)):
            arr[i] = li_3[i]