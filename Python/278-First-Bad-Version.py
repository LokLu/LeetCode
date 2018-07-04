# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        middle = (start+end)/2
        while end>start:
            
            middle = (start+end)/2
            if isBadVersion(middle)==True:
                end = middle
            else:
                start = middle+1

        return start
        
        
