class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range (0,len(nums)):
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
            
        return [x+1 for x,y in enumerate(nums) if y>0]
