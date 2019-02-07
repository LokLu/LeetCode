class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        tmp = bin(n)
        ele = list(set(list(tmp[3:])))
        return tmp[2]=='1' and ele==[] or ele==['0'] 
