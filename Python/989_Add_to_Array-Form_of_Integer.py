class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        i=-1
        carry = 0
        result = []
        while K>0 or -i<=len(A) or carry!=0:
            if -i>len(A):
                dig_A = 0
            else:
                dig_A = A[i]
                
            dig = dig_A + K%10 + carry
            result.insert(0,dig%10)
            K=K/10
            carry = dig/10
            i-=1

        return result
