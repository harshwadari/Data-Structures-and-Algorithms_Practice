# Generate all binary string
"""
Given an integer n. You need to generate all the binary strings of n characters representing bits.

Note: Return the strings in  ascending order.

Examples:

Input: n = 2
Output: [00, 01, 10, 11]
Explanation: As each position can be either 0 or 1, the total possible combinations are 4.
"""

# Optimal approach using recursion backtracking
# TC = O(2^N) and SC = O(N)
def binstring(n: int) -> list[str]:
    result = []
    def backtrack(index: int,string: list[str])-> list[int]:
        if index == n:
            result.append(''.join(string))
            return
        string.append('0')
        backtrack(index + 1,string)
        string.pop()
        string.append('1')
        backtrack(index + 1,string)
        string.pop()
    backtrack(0,[])
    return result


#Binay String for consecutive 1's
# TC = O(2^N) and SC = O(N)
def generateBinaryStrings(self, n):
    ans = []
    def backtrack(index, string):
        if index == n:
            ans.append("".join(string))
            return
        # Always place 0
        string.append('0')
        backtrack(index + 1, string)
        string.pop()
        # Place 1 only if previous is not 1
        if len(string) == 0 or string[-1] != '1':
            string.append('1')
            backtrack(index + 1, string)
            string.pop()
    backtrack(0, [])
    return ans