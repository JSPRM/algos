

class Solution:
    def mergeTwoLists(self,l1: list[int], l2: list[int]) -> list:
        n1,n2 = len(l1), len(l2)
        i,j,k = 0,0,0
        l3 = [None] * (n1+n2)
        
        while i < n1 and j < n2:
            if l1[i] < l2[j]:
                l3[k] = l1[i]
                k+=1
                i+=1
            else:
                l3[k] = l2[j]
                k+=1
                j+=1
                
        while i < n1:
            l3[k] = l1[i]
            k+=1
            i+=1
            
        while j < n2:
            l3[k] = l2[j]
            k+=1
            j+=1
        
        return l3   
                