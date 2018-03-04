class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(digits)-1,-1,-1):
            if i ==len(digits)-1:
                digits[-1],carry=(digits[-1]+1)%10,(digits[-1]+1)/10
            else:
                digits[i],carry=(digits[i]+carry)%10,(digits[i]+carry)/10

        if carry ==1:
            digits.insert(0,carry)
                
        return digits
            
