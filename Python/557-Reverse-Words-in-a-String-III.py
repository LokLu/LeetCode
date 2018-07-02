class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split(' ')        
        while '' in words:
            words.remove('')
        
        
        for i in range (0,len(words)):
            words[i]=words[i][::-1]
        
        return ' '.join(x for x in words)
