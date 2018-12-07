class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if len(A)<3:
            return False 
        
        i = 0
        while i < len(A)-1:
            if A[i+1] > A[i]:
                i+=1
            else:
                break
            
        if i==0 or i==len(A)-1:
            return False
    
        while i< len(A)-1:
            if A[i+1] < A[i]:
                i+=1
            else:
                break

        return i==len(A)-1
