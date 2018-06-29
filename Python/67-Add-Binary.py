class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = len(a)-1
        num_b = len(b)-1
        carry = 0
        result = 0
        index = 1
        while num_a>=0 or num_b>=0:
            if num_a < 0:
                new = int(b[num_b])+carry
            elif num_b <0:
                new = int(a[num_a])+carry
            else:  
                new = int(a[num_a])+int(b[num_b])+carry
            carry = new/2
            result += index*(new%2)
            num_a-=1
            num_b-=1
            index*=10
            
        result += index*carry
        
        return str(result)
