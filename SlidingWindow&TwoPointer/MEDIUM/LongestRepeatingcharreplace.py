# 424. Longest Repeating Character Replacement

# brute force approach 
# TC = O(N^2) and SC = O(26)
class Solution(object):
    def characterReplacement(self, s, k):
        maxlen = 0
        
        for i in range(len(s)):
            freq = [0] * 26
            maxfreq = 0
            
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord('A')
                freq[idx] += 1
                
                maxfreq = max(maxfreq, freq[idx])
                
                change = (j - i + 1) - maxfreq
                
                if change <= k:
                    maxlen = max(maxlen, j - i + 1)
                else:
                    break
        
        return maxlen