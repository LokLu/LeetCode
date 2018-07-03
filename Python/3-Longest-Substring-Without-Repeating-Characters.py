class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        tmp_str = ''
        for i in range(len(s)):
            if s[i] in tmp_str:
                tmp_str = tmp_str[tmp_str.find(s[i])+1:]+s[i]
            else:
                tmp_str +=s[i]
                length = max(length,len(tmp_str))
                
        return length
