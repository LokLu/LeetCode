class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        d = {'I': 1,'V': 5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        if len(s)==0:
            return 0
        
        for i in range (len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                result -=d[s[i]]
            else:
                result +=d[s[i]]
        result = result+d[s[-1]]
        
        return result
