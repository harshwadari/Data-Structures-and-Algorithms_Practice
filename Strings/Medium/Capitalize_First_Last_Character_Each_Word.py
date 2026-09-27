# Capitalize First and Last Character of Each Word
"""
You are given a string s consisting of one or more words separated by single spaces. 
Your task is to capitalize the first and last character of each word in the string.

If a word contains only one character, capitalize that character.

Return the transformed string after applying the operation to all words.

Example 1:
Input: s = "take u forward is awesome"

Output: "TakE U ForwarD IS AwesomE"

Explanation: Each word's first and last characters are capitalized.

Example 2:
Input: s = "Take u Forward is Awesome"

Output: "TakE U ForwarD IS AwesomE"

Explanation: Already capitalized characters remain, others are capitalized.




Constraints:
1 <= s.length <= 10^5
The string contains only lowercase and uppercase English letters and single 
spaces between words
There are no leading or trailing spaces, and no multiple spaces between words
"""

"""
split()     O(N)
for loop    O(N)
join()      O(N)
----------------
Total       O(3N)
space = O(N)
"""
# Optimal Approch using splitting
def capitalize(s:str) -> str:
    words = s.split()
    for i in range(len(words)):
        word = words[i]
        if len(word) == 1:
            words[i] = word.upper()
        else:
            words[i] = word[0].upper() + word[1:-1] + word[-1].upper()
    return " ".join(words)



# Another appraoch 
class Solution:
    def capitalizeWords(self, s):
        s = list(s)

        n = len(s)

        for i in range(n):
            if i == 0 or s[i - 1] == ' ':
                s[i] = s[i].upper()

            if i == n - 1 or s[i + 1] == ' ':
                s[i] = s[i].upper()

        return ' '.join(s)