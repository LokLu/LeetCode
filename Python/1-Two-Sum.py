class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = [0, 0]
        num_list = len(nums)
        for i in range (num_list):
            
            for j in range (i+1,num_list):
                
                if nums[i]+nums[j]==target:
                    result[0]=i
                    result[1]=j
                    break
                if j == num_list-1:
                    print 'No matching solutions were found'
                
        return result
