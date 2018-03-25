class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minv = float('inf')
        maxp = 0        
        for i in range (0,len(prices)):
            minv = min(minv,prices[i])
            maxp = max(maxp,prices[i]-minv)
 
        return maxp
