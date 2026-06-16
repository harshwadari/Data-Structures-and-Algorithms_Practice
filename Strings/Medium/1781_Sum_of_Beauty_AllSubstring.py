# 1781. Sum of Beauty of All Substrings


# Brute approach by generating all substring and checking for beauty
# TC - O(N^3) and SC = O(26) = O(1)
def beautySum(s:list[str])-> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                freq = {}
                for k in range(i,j+1):
                    char = s[k]
                    if char in freq:
                        freq[char] += 1
                    else:
                        freq[char] = 1
                mx = max(freq.values()) 
                mn = min(freq.values())
                ans += mx - mn
        return ans

# Optimal approach 
# TC = O(N^2) and SC = O(1)
def beautySum(self, s):
        # Code here
        result = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i , len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                mx = 0
                mn = float('inf')
                for k in freq:
                    if k > 0:
                        mx = max(mx,k)
                        mn = min(mn,k)
                result += mx - mn
        return result