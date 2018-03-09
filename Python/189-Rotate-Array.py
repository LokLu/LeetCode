class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if k!=0:
            k = k%len(nums)
            if k!=0:
                for i in range (0,(len(nums)-k+1)/2):
                    nums[i],nums[len(nums)-k-1-i]=nums[len(nums)-k-1-i],nums[i]
                for i in range (len(nums)-k,(2*len(nums)-k-1)/2+1):
                    nums[i],nums[2*len(nums)-k-1-i]=nums[2*len(nums)-k-1-i],nums[i]
                # nums[0:k+1].reverse()
                # nums[k+1:-1].reverse()
                nums.reverse()
