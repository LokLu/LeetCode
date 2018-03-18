class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left=right = 0
        total = sum(nums)
        
        for i in range (0, len(nums)):
            right = total-left-nums[i]
            if left==right:
                return i
            left +=nums[i]
        
        return -1
