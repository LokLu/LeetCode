class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        maximum = nums[0]
        for i in range (1,len(nums)):
            new_dp = nums[i]+(dp[i-1] if dp[i-1]>0 else 0)
            dp.append(new_dp)
            maximum = max(maximum,dp[i])
            
        return maximum
