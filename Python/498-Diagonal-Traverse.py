class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        upright = 1
        result = []
        i = j = 0
        
        h = len(matrix)
        if h ==0:
            return result
        w = len(matrix[0])

        while (i < h and j < w):
            result.append(matrix[i][j])
            if upright:
                if i-1>=0 and j+1<w:
                    i-=1
                    j+=1
                else:
                    upright = 0
                    if i-1<0 and j+1<w:
                        j = j+1  
                    else:
                        i = i+1
            else:
                if i+1<h and j-1>=0:
                    i+=1
                    j-=1                   
                else:
                    upright = 1
                    if i+1<h and j-1<0 :
                        i+=1
                    else:
                        j+=1
                        
        return result
