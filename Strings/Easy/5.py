# 796. Rotate String


"""
Docstring for Strings.Easy.5

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
"""


# brute force 
# TC = O(N^2) and SC = O(N) N^2 due to slicing

def rotate(s,goal):
    if len(s) != len(goal):
        return False
    curr = s
    for i in range(len(curr)):
        if curr == goal:
            return True
        curr = curr[-1] + curr[:-1]
    return False




# otpimal approach

def rotateString(s,goal):
    if len(goal) != len(s):
        return False
    