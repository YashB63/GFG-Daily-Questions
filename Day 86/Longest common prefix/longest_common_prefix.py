class Solution:
    def longestCommonPrefix(self, str1, str2):
        
        s=''
        st=-1
        end=-1
        check=False
        for  ind,i in enumerate(str1):
           s+=i
           if s in str2:
               if not check:
                   st=ind
                   check=True
               end=ind
           else:
               break;
        return (st,end)