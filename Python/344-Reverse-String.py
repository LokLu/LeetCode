class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range (0,len(s)/2):
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
            
        return "".join(str(x) for x in s)
