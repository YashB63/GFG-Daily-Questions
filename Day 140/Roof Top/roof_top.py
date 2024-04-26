class Solution:
    
    def maxStep(self,a, n):
        
        all_steps = []
        steps = 0
        for i in range(1,n):
            if a[i-1] < a[i]:
                steps = max(steps,1)
                if i >= 2:
                    if a[i-2] < a[i-1]:
                        steps += 1
            else:
                steps = 0
            all_steps.append(steps)
        if all_steps:
            return max(all_steps)
        else:
            return 0