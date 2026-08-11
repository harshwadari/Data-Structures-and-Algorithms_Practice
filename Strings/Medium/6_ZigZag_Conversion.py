# 6. Zigzag Conversion
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


# Brute Force Appraoch 
"""

Input:
s = "PAYPALISHIRING"
numRows = 3

Matrix:
P . . . A . . . H . . . N
A . P . L . S . I . G
Y . . I . . . R
Then read it row by row.

Think about these 4 things while coding
How big should your matrix be?
Where does the current character go?
How do you move down?
How do you move up-right?
"""

# TC = O(N ^ 2) and SC = O(N ^ 2)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1:
            return s
        mat = [['.'] * n for _ in range(n)]
        row = 0
        col = 0
        direction = 1
        for char in s:
            mat[row][col] = char
            if direction == 1:
                if row == numRows - 1:
                    direction -= 1
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                if row == 0:
                    direction = 1
                    row += 1
                else:
                    row -= 1
                    col += 1
        result = []
        for i in range(numRows):
            for j in range(n):
                if mat[i][j] != '.':
                    result.append(mat[i][j])
        return "".join(result)
            

#Optimal Approach 
# TC = O(N) and SC = O(N)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        row = 0
        direction = 1
        rows = [""] * numRows
        for char in s:
            rows[row] += char
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1
            row += direction
        return "".join(rows)
