class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        if len(nums)*len(nums[0])!=r*c:
            return nums
        else:
            result = [[]]*r
            all=[]
            for i in range (0,len(nums)):
                all.extend(nums[i])
            for j in range (0,r):
                result[j]=all[j*c:(j+1)*c]
            return result   
