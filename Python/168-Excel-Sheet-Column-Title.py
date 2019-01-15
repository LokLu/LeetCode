class Solution(object):
    
    def numToChar(self, s):
        #chr(65)='A'
        return chr(s+64)
    
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        tmp = n
        if tmp==0:
            return ""
        while tmp>26:
            index = tmp%26
            if index ==0: index=26 
            result.insert(0, self.numToChar(index))
            tmp = int(tmp-index)/26
        index = tmp%26
        if index ==0: index=26 
        result.insert(0, self.numToChar(index))            
        return ''.join(result)
