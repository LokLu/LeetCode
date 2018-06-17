class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R = []
        for row in A:
            for x in range (0,(len(row)+1)/2):
                # if x!=len(row)-1-x:
                tmp = row[x]
                row[x] = 1 - row[len(row)-1-x]
                row[len(row)-1-x]= 1-tmp
                # else:
                #     row[x]=1-row[x]
            R.append(row)                    
        return R
