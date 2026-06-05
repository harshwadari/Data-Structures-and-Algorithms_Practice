# 28. Find the Index of the First Occurrence in a String

# brute force approach is to check all possible patterns in given string and check if it matches with the given pattern
# TC = O(N*M) and SC = O(1)

def strSearch(string,pattern):
    n = len(string)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and string[i + j] == pattern[j]:
            j += 1
        if j == m :
            return i
    return - 1


# better / optimal approach using knuth morris pratt string searching algorithm
#TC = O(N + M) and SC = O(1)

def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        lps = [0] * len(needle)
        length = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        i = 0
        j = 0
        while i <  len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1
        return - 1

