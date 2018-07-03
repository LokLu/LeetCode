class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        
        new_number=0
        
        singal = abs(x)/x
        x = abs(x)
        
        while x>0:
            new_number = 10*new_number+x%10
            x = x/10
        
        new_number *= singal
        
        if new_number<-pow(2,31) or new_number>pow(2,31):
            return 0
        
        return new_number
