class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max1=max2 = -1
        index = -1
        for i in range (0,len(nums)):
            if max1<nums[i]:
                max1,max2 = nums[i],max1
                index =i
            else:
                max2 = max(max2,nums[i])
                
        return index if max1>=max2*2 else -1
