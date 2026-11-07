# 709. To Lower Case
"""
Given a string s, return the string after replacing every uppercase 
letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""

# approach using built in function 
# TC = O(N) and SC = O(N)
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for char in s:
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char)
        return "".join(result)


# appraoch using ascii values
# TC = O(N) and SC = O(N)
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for char in s:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return "".join(result) 





result = []
def take(s):
    for char in s:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(char) + 32))
    
        elif 'a' <= char <= 'z':
            result.append(chr(ord(char) - 32))
    
        else:
            result.append(char)
    
    return "".join(result)