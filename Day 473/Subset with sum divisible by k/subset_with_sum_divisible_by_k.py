class Solution:
	def DivisibleByM(self,arr, k):
        n = len(arr)
        modseen = bytearray(k)
        modseen[arr[0] % k] = 1
        for i in range(1, n):
            oldmod = modseen
            modseen = bytearray(modseen)
            x = arr[i] % k
            modseen[x] = 1
            for r in range(k):
                if oldmod[r]:
                    modseen[(x + r) % k] = 1
            if modseen[0]: break
        return modseen[0]