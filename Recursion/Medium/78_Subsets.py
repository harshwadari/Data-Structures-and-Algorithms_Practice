# 78. Subsets / Print all subsequences of given array 

"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


# Optimal Approach using Recursion Backtracking 
"""

Time Complexity: O(n × 2ⁿ)
Why?

There are 2 choices for every element:

Pick
Not Pick

So the recursion tree has:

2^n leaf nodes

At every leaf, you execute:

result.append(subset[:])

Copying subset[:] takes O(n) in the worst case.

So:

Number of subsets × Time to copy each subset
= 2^n × O(n)
= O(n × 2^n)
Time Complexity: O(n × 2^n) because there are 2^n subsets and copying each subset takes up to O(n).
Auxiliary Space: O(n) due to the recursion stack and the current subset.
Space Including Output: O(n × 2^n) because all subsets are stored.
"""

def subsets(nums:list[int]) -> list[list[int]]:
    result = []
    def backtrack(idx: int, subset:list[int]) -> None:
        if idx >= len(nums):
            result.append(subset[:])
            return 
        #pick
        subset.append(nums[idx])
        backtrack(idx + 1,subset)
        # not pick 
        subset.pop()
        backtrack(idx + 1, subset)
    backtrack(0,[])
    return result
    

# same problem for strings subsequence

"""
At every leaf, you're storing a string.

Average string length can be O(n).

So:

TC = O(n × 2^n)

If you do:

result.sort()

after generating all subsequences:

Number of strings = 2^n

Sorting cost:

O(2^n × log(2^n))
= O(2^n × n)

String comparisons can take up to O(n), so technically:

Sorting = O(n² × 2^n)

Therefore the overall complexity becomes:

TC = O(n² × 2^n)

because sorting dominates.

Space Complexity

Recursion stack:

O(n)

Output storage:

2^n strings

Each string can be length O(n).

Therefore:

Output Space = O(n × 2^n)

Total:

SC = O(n × 2^n)

(excluding output, recursion stack alone is O(n)).

Interview answer

If they ask:

TC = O(n × 2^n) for generating
TC = O(n² × 2^n) if final sorting is included

SC = O(n) auxiliary
SC = O(n × 2^n) including output
"""

def powerSet(s:list[str]) -> list[list[str]]:
    result = []
    def solver(idx, subset):
        if idx >= len(s):
            result.append(subset)
            return
        solver(idx + 1, subset + s[idx])  # pick
        solver(idx + 1, subset)           # not pick
    solver(0, "")
    return result