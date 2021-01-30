# Time Limit Exceeded
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        def dp(n):
            if n<0: return -1
            if n==0: return 0
            least_num = float('INF')
            for coin in coins:
                tmp = dp(n-coin)
                if tmp==-1: continue
                least_num = min(least_num, 1+dp(n-coin))
                
            if least_num==float('INF'):
                return -1
            else:
                return least_num
        
        return dp(amount)
