class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = n
        num_list = []
        while tmp!=1:
            tmp = self.sum_digits(tmp)
            if tmp in num_list:
                return False
            else:
                num_list.append(tmp)
        
        return True
            
    def sum_digits(self, n):
        tmp = 0
        for x in str(n):
            tmp += int(x)*int(x)
            
        return tmp
