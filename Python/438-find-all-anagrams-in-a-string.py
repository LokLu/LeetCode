class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        result = []
        left,right = 0,0
        
        needs = Counter(p)
        windows = collections.defaultdict(int) 
        match = 0
        
        while right<len(s):
            
            c_right = s[right]
            
            if needs[c_right]>0:
                windows[c_right]+=1
                if windows[c_right]==needs[c_right]:
                    match+=1
            right+=1
            
            while match ==len(needs):
                
                if len(p)==len(s[left:right]):
                    result.append(left)
                c_left = s[left]
                if needs[c_left]>0:
                    windows[c_left]-=1
                    if windows[c_left]<needs[c_left]:
                        match-=1
                left+=1
                
        return result
