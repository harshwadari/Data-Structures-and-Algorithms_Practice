# 3838. Weighted Word Mapping

# TC = O(T) where t is total no of char in words and SC = O(N) 

def mapwordwieghts(words,weights):
    result = ""
    for word in words:
        total = 0
        for ch in word:
            idx = ord('ch') - ord('a')
            total += weights[idx]
        rem = total % 26
        result += chr(ord('z') - rem)
    return result