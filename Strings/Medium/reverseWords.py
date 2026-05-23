#151. Reverse Words in a String

# brute force using split and reverse
# TC = O(N) and SC = O(N)
def reverseWords(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
print(reverseWords("hello world"))

# optimal approach using two pointer
# TC = O(N) and SC = O(N)
def reverseWordsOptimal(s):
    words = []
    word = ""
    
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    
    if word:
        words.append(word)
    
    left, right = 0, len(words) - 1
    
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    
    return " ".join(words)
print(reverseWordsOptimal("hello world"))