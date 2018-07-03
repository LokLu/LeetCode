class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n==1:
            return '1'
        
        tmp = self.countAndSay(n-1)
        result = ''
        index = 0
        status = tmp[0]
        num = 0

        while index<(len(tmp)):
            if tmp[index]==status:
                num+=1
            else:
                result = result + str(num)+status
                status = tmp[index]
                num = 1
            index = index+1
        result = result + str(num)+status
            
        return result
