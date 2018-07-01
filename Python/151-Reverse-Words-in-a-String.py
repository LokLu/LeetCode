class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split(' ')
        words = words[::-1]
        
        while '' in words:
            words.remove('')
            
        return ' '.join(x for x in words)
