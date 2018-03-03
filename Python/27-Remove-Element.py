class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        total = len(nums)
        start_index = 0
        while start_index <total:
            if nums[start_index]==val:             
                nums[start_index:-1]=nums[start_index+1:]
                total-=1
            else:
                start_index +=1
                
        return start_index
