class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i=0
        while i < len(s):
            if s.count(s[i])==1:
                return i
            i+=1
        return -1
