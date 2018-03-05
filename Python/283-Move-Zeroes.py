class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        count = nums.count(0)
        
        for i in range (0,count):
            nums.append(nums.pop(nums.index(0)))
