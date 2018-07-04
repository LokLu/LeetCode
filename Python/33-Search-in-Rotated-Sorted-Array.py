class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start,end = 0,len(nums)-1
        
        
        while end-start>=0:
            middle = (start+end)/2
            print start,end,middle
            if nums[start]==target:
                return start 
            if nums[end]==target:
                return end 
            if nums[middle]==target:
                return middle 
        
            # if nums[middle]>target:
            #     if nums[start]<target:
            #         end = middle-1
            #     elif nums[start]>target:
            #         start = middle+1
            # elif nums[middle]<target:
            #     if nums[end]<nums[middle]:
            #         start = middle+1
            #     elif nums[end]>target:
            #         start = middle+1
            # else:
            #     return middle
                    
        
            if nums[start]<target and nums[middle]>target:
                end = middle-1
            elif nums[middle]<target and nums[end]>target:
                start = middle+1
            elif nums[start]>nums[middle] and (nums[start]<target or nums[middle]>target):
                end = middle-1
            elif nums[end]<nums[middle] and (nums[end]>target or nums[middle]<target):
                start = middle+1
            else:
                return -1
            
        return -1
        
