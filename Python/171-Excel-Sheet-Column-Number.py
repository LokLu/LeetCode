class Solution(object):
    
    def chrToNumber(self, s):
        #chr(65)='A'
        return ord(s)-64
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        for i in range (len(s)):
            num = 26**i* self.chrToNumber(s[len(s)-1-i])+num
            
        return num
