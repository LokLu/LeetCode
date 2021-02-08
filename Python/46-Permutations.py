class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []
        
        def backtrack(nums,track):
            if len(track)==len(nums):
                res.append(track.copy())
                return

            for i in range (0,len(nums)):
                if nums[i] in track:
                    continue

                track.append(nums[i])
                backtrack(nums,track)
                track.pop(-1)
        
        backtrack(nums,track)

        return res
    

        
