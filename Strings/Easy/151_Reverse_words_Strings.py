# 151. Reverse Words in a String

"""
Docstring for Strings.Easy.2


Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated 
by a single space.
Note that s may contain leading or trailing spaces or multiple 
spaces between two words. The returned string should 
only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
"""



# brute force using python powers
# TC = O(N) and SC = O(N)
def reverseWords(s):
    words = s.split()
    words.reverse()
    result = " ".join(words)
    return result
print(reverseWords("The Sky is Blue"))



# optimal approach 
# TC = O(N) and  SC = O(1) ignoring result ouput
def reverse(s):
    n = len(s)
    result = ""
    i = n-1
    while i >=0:
        while i >=0 and s[i] == " ":
            i -=1
        if i <0:
            break
        j = i
        while i >= 0 and s[i] != " ":
            i -=1
        if result:
            result += " "
        result += s[i+1:j+1]
    return result