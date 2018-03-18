class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = average = sum(nums[0:k])

        for i in range (1, len(nums)-k+1):
            # average = sum(nums[i:i+k])
            average = average-nums[i-1]+nums[i+k-1]
            result = max(result,average)
            
        return float(result)/k
