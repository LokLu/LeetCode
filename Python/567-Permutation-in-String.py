class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        result = False
        
        left = right = 0
        needs = Counter(s1)
        windows = collections.defaultdict(int)
        match = 0
        
        while right<len(s2):
            bot = s2[right]
            if needs[bot]>0:
                windows[bot]+=1
                if windows[bot]==needs[bot]:
                    match+=1
            right+=1
        
            while match == len(needs):
                if len(s1)==len(s2[left:right]):
                    return True
                top = s2[left]
                if needs[top]>0:
                    windows[top]-=1
                    if windows[top]<needs[top]:
                        match-=1
                left+=1
            
        return result
                    
        
