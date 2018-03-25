class Solution(object):
      
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
    
        by = 0
        skip = 0
        for i in range (len(cost)-1,-1,-1):
            by,skip = cost[i]+min(by,skip),by
            
        return min(by,skip)
