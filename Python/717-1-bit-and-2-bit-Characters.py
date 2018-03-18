class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        char = -1
        i =0
        while i < len(bits):
            if bits[i]==1:
                char = 2
                i+=2
            else:
                char = 1
                i+=1
                
        return True if char == 1 else False
