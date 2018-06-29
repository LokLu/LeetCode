class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num = 0
    
        if strs==[]:
            return ''
        
        while 1:
            for i in range (0,len(strs)):
                if num>=len(strs[i]) or strs[0][num] != strs[i][num]:
                    return strs[0][0:num]
            num+=1
            
