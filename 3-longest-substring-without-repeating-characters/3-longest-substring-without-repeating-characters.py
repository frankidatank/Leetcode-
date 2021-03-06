class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #tip here is to only move left but not add to set, sliding window
        st = set()
        l,r = 0,0
        res = 0
        while r < len(s):
            rch = s[r]
            if rch not in st:
                st.add(rch)
                res = max(res, len(st))
                r += 1
            else:
                lch = s[l]
                st.remove(lch)
                l += 1
        return res
                
                
            
                
                
            
                
                
                
            
        
    
            
          
        

