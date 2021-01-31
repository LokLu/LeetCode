# liner time
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = len(nums)
        end = -1
        for i in range (0,len(nums)):
            if nums[i] ==target:
                start = min(start,i)
                end = max(end,i)
        
        if start==len(nums):
            return [-1,-1]
        else:
            return [start,end]
