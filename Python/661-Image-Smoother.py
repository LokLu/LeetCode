class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = []
        h, w = len(M), len(M[0])

        for i in range (0, h):
            row = [None]*w
            
            for j in range (0, w):
                starth = i-1 if i>1 else 0
                endh = i+1 if i<h-1 else h-1
                startw = j-1 if j>1 else 0
                endw = j+1 if j<w-1 else w-1
                num = (endw-startw+1)*(endh-starth+1)
                aera = 0
                for x in range (starth,endh+1):
                    aera = aera+sum(M[x][startw:endw+1])
                row[j]=aera/num
                
            result.append(row)
            
        return result
