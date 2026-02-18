class Solution:
    def maxProduct(self,arr):
        cmx=1
        gmx=png=-float('inf')
        zer=False
        for v in arr:
            if v==0:
                cmx=1
                png=-float('inf')
                zer=True
                continue
            cmx*=v
            gmx=max(gmx,cmx,(cmx//png if png!=-float('inf') else -float('inf')))
            if cmx<0:
                png=max(png,cmx)
        return max(gmx,(0 if zer else -float('inf')))