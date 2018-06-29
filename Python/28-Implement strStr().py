class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '':
            return 0
        
        for i in range (0,len(haystack)-len(needle)+1):
            for j in range (0,len(needle)):
                if needle[j]!=haystack[i+j]:
                    break
                elif j == len(needle)-1:
                    return i
                
        return -1
