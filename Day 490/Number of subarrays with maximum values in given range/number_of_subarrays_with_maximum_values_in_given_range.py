class Solution:
    def countSubarrays(self, a,n,L,R): 
        def count_sub_array(size):
            return size*(size+1)//2
            
        smaller_L = 0
        smaller_R = 0
        
        count = 0
        
        for i in range(n):
            if arr[i]>R:
                count+=count_sub_array(smaller_R)-count_sub_array(smaller_L)
                smaller_L = 0
                smaller_R = 0
            elif arr[i] < L:
                smaller_L += 1
                smaller_R += 1
            else:
                count-=count_sub_array(smaller_L)
                smaller_L=0
                smaller_R += 1       
        count+=count_sub_array(smaller_R)-count_sub_array(smaller_L)
    
        return count