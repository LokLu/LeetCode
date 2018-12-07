class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        start,end = 0, len(x)-1
        
        while end-start>0:
            if x[start]==x[end]:
                start+=1
                end-=1
            else:
                return False

        return True
