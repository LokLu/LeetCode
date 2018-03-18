class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=count = 0
        
        for i in range (0, len(nums)):
            if i==0: 
                count +=1 
            elif nums[i]>nums[i-1]:
                count +=1
            else: 
                count = 1
            length = max(count,length)
            
        return length
