class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        if '1' in digits or len(digits)==0:
            return []
        
        result = ['']
        for i in range (len(digits)):
            tmp = result
            result = []
            for new in d[digits[i]]:
                for x in tmp:
                    result.append(x+new)
            
        return result
