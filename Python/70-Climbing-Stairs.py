class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1,1]
    
        while len(result)<n+1:
            result.append(result[-1]+result[-2])
            
        return result[-1]
