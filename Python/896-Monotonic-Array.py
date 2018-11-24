class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sign = 0
        for i in range(1, len(A)):
            if sign==0:
                sign = A[i]-A[i-1]
            tmp = A[i]-A[i-1]
            if tmp*sign<0:
                return False
        return True
