class Solution:
    def search(self, arr, x):
        
        l=0
        u=len(arr)-1
        m=0
        
        while l<=u :
            m = l+(u-l)//2 

            if arr[m] == x :
                return m
            
            elif arr[m] >= arr[l] :

                # sorted part is left-side of middle
                if x >= arr[l] and x < arr[m]: 
                    u = m-1
                
               # sorted part is right-side of middle
                else:                          
                    l = m+1
            else:

                # sorted part is right-side of middle
                if x <= arr[u] and x > arr[m]:
                    l = m+1                    
                
                # sorted part is left-side of middle
                else:
                    u = m-1                    
        return -1