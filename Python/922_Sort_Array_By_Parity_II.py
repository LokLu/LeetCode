class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        for i in range(0, len(A)):
            odd = i%2
            if A[i]%2 == odd:
                continue
            else:
                while A[i]%2 != odd:
                    A.append(A.pop(i))
                    
        return A
