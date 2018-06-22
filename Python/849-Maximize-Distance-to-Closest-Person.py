class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_0 = 0
        start = -1
        
        for i in range (0,len(seats)):

            if seats[i]!=0:
                if start==-1:
                    distance = i-start-1
                else:
                    distance = (i-start)/2
                
                max_0 = max(max_0, distance)
                start =  i
        
        if seats[-1]==0:
            max_0 = max(max_0,len(seats)-1-start)
            
        return max_0
