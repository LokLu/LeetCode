class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_min = nums[-1]
        num_max = nums[0]
        begin = len(nums)-1
        end = 0
        n=len(nums)
        
        for i in range (n):
            num_min = min(nums[n-1-i],num_min)
            if nums[n-1-i]>num_min:
                begin = n-1-i
            num_max = max(nums[i],num_max)
            if nums[i]<num_max:
                end = i
                
        if end>begin:
            return end-begin+1
        else:
            return 0
