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

    
# With memorey storing computed amount
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        num_dict = dict()
        
        def dp(n):
            if n in num_dict: return num_dict[n]
            if n<0: return -1
            if n==0: return 0
            least_num = float('INF')
            for coin in coins:
                tmp = dp(n-coin)
                if tmp==-1: continue
                least_num = min(least_num, 1+dp(n-coin))
                
            if least_num==float('INF'):
                num_dict[n]=-1
                return -1
            
            else:
                num_dict[n]=least_num
                return least_num
            
        return dp(amount)
