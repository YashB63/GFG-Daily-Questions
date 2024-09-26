class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        mel=height[0]
        c=1
        for i in range(1,len(height)):
            if mel<height[i]:
                c+=1
                mel=height[i]
        return c