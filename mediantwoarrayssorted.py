class Solution:
    def findMedianSortedArrays(self,nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if(n2<n1):
            return self.findMedianSortedArrays(nums2,nums1)
        
        menor, mayor = 0, n1
        
        while(menor<=mayor):
            corte1 = (menor + mayor)//2
            corte2 = (n1+n2+1)//2 - corte1
            
            izq1 = float("-inf") if (corte1 == 0) else nums1[corte1-1]
            izq2 = float("-inf") if (corte2 == 0) else nums2[corte2-1]
        
            der1 = float("+inf") if (corte1 == n1) else nums1[corte1]
            der2 = float("+inf") if (corte2 == n2) else nums2[corte2]
            
            
            if(izq2 <= der1 and izq1 <= der2):
                if((n1+n2)%2 == 0):
                    return (max(izq1,izq2)+min(der1,der2))/2
                return max(izq1,izq2)
            elif(der2 < izq1):
                mayor = corte1 - 1
            else:
                menor = corte1 + 1