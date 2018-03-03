class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        last_number = None
        while index < len(nums):
            if nums[index]!=last_number:
                last_number = nums[index]
                index  = index +1
            else:
                del nums[index]
                
        return len(nums)
    
