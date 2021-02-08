class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left = right = 0
        needs = Counter(t)
        windows = collections.defaultdict(int)
        match = 0
        minleft = 0
        minright = len(s)+1
        
        while right<len(s):
            bot = s[right]
            if needs[bot]>0:
                windows[bot] +=1
                if needs[bot]==windows[bot]:
                    match+=1
            
            right+=1
            
            while match == len(needs):
                # print(left,right)
                top = s[left]
                if needs[top]>0:
                    windows[top]-=1
                    if windows[top]<needs[top]:
                        match -=1
                        length = right-left
                        if length<minright-minleft:
                            minright = right
                            minleft = left
                left+=1
        # print(minleft,minright,left,right)
        return '' if minright-minleft == len(s)+1 else s[minleft:minright]
                
                
        
