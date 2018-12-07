class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        
        char_dict = {")":"(","]":"[","}":"{"}
        
        for char in s:
            if tmp == [] or char not in char_dict.keys():
                tmp.append(char)
            elif tmp[-1]==char_dict[char]:
                    tmp.pop()
            else:
                tmp.append(char)
            
        return tmp==[]
