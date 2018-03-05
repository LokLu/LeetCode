class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = 0
        for i in range (0,len(nums)+1):
            s+=i
            
        return s-sum(nums)
