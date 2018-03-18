class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.append(0)
        start = end = 0
        num_total = 0
        
        for i in range (1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0:
                end+=1
            elif flowerbed[i]==1 and flowerbed[i-1]==0:
                num = (end-start)/2
                num_total += num
                start = end
            elif flowerbed[i]==0 and flowerbed[i-1]==1:
                start=end=i
        
        end+=1
        num = (end-start)/2
        num_total += num
        
        return True if n<= num_total else False
